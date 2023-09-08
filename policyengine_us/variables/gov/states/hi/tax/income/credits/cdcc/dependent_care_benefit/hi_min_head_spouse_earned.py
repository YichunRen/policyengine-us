from policyengine_us.model_api import *


class hi_min_head_spouse_earned(Variable):
    value_type = float
    entity = TaxUnit
    label = "Hawaii minimum income between head and spouse for the CDCC"
    defined_for = StateCode.HI
    unit = USD
    definition_period = YEAR
    reference = (
        "https://files.hawaii.gov/tax/forms/2022/n11ins.pdf#page=28"
        "https://files.hawaii.gov/tax/forms/2022/n11ins.pdf#page=29"
        "https://files.hawaii.gov/tax/legal/hrs/hrs_235.pdf#page=41"
        "https://files.hawaii.gov/tax/forms/2022/schx_i.pdf#page=2"
    )

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.hi.tax.income.credits.cdcc
        person = tax_unit.members
        head = person("is_tax_unit_head", period)
        spouse = person("is_tax_unit_spouse", period)
        head_or_spouse = head | spouse
        eligible = head_or_spouse & (
            person("is_disabled", period)
            | person("is_full_time_student", period)
        )
        qualified_children = tax_unit("count_cdcc_eligible", period)
        income = person("earned_income", period)
        one_child_floor = max_(
            p.dependent_care_benefits.expense_floor.one_child,
            head_or_spouse * income,
        )
        two_or_more_children_floor = max_(
            p.dependent_care_benefits.expense_floor.two_or_more_child,
            head_or_spouse * income,
        )
        total_floor_amount = where(
            qualified_children <= 1,
            one_child_floor,
            two_or_more_children_floor,
        )
        eligible_income = where(
            eligible,
            total_floor_amount,
            head_or_spouse * income,
        )
        # remove impact of smaller income not belong to head/spouse
        head_spouse_income = where(
            head_or_spouse, eligible_income, tax_unit.max(eligible_income)
        )
        # Edge case: both spouses were students or disabled:
        # compare original income with eligible income
        both_disabled_income = where(
            head_or_spouse,
            min_(head_or_spouse * income, eligible_income),
            head_spouse_income,
        )
        # take the minumum of original income if both incomes below the floor
        reach_income_floor = (head_or_spouse * income) < eligible_income
        head_spouse_income = where(
            (sum(eligible) == 2) & (sum(reach_income_floor) == 2),
            both_disabled_income,
            head_spouse_income,
        )

        return tax_unit.min(head_spouse_income)
