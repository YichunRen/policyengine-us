from policyengine_us.model_api import *


class ga_retirement_income(Variable):
    value_type = float
    entity = Person
    label = "Georgia retirement income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.georgia.gov/document/booklet/2021-it-511-individual-income-tax-booklet/download"
        "https://dor.georgia.gov/document/document/2022-it-511-individual-income-tax-booklet/download"
        "https://advance.lexis.com/documentpage/?pdmfid=1000516&crid=fb5db531-a80f-4790-bddb-eefc8327ef60&config=00JAA1MDBlYzczZi1lYjFlLTQxMTgtYWE3OS02YTgyOGM2NWJlMDYKAFBvZENhdGFsb2feed0oM9qoQOMCSJFX5qkd&pddocfullpath=%2Fshared%2Fdocument%2Fstatutes-legislation%2Furn%3AcontentItem%3A65D2-CDH3-CGX8-044N-00008-00&pdcontentcomponentid=234186&pdteaserkey=sr1&pditab=allpods&ecomp=8s65kkk&earg=sr1&prid=66f02b0a-c5ae-4162-9535-127751546807"
    )
    defined_for = StateCode.GA
    adds = (
        "gov.states.ga.tax.income.agi.exclusions.retirement.retirement_income"
    )
