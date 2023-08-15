from policyengine_us.model_api import *


class adjusted_gross_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Federal adjusted gross income for each tax unit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/62"

    def formula(tax_unit, period, parameters):
        gross_income = add(tax_unit, period, ["irs_gross_income"])
        above_the_line_deductions = tax_unit(
            "above_the_line_deductions", period
        )
        agi = gross_income - above_the_line_deductions
        if parameters(period).gov.contrib.ubi_center.basic_income.taxable:
            agi += add(tax_unit, period, ["basic_income"])
        return agi
