from policyengine_us.model_api import *


class is_grandparent_of_filer_or_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Is a grandparent of the filer or the spouse of the filer"
    definition_period = YEAR
