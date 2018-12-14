import ptest

@ptest.hookimpl
def ptest_add_ingredients():
    spices = ["salt", "pepper"]
    you_can_never_have_enough_eggs = ["egg", "egg"]
    ingredients = spices + you_can_never_have_enough_eggs
    return ingredients

@ptest.hookimpl
def ptest_prep_condiments(condiments):
    condiments["mint sauce"] = 1