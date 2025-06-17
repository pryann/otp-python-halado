def add_bacon(burger):
    burger["bacon"] = True
    return burger


def add_double_meal(burger):
    burger["doubleMeal"] = True
    return burger


def add_cheese(burger):
    burger["cheese"] = True
    return burger


def add_gluten_free_bun(burger):
    burger["glutenFreeBun"] = True
    return burger


def remove_onion(burger):
    burger["onion"] = False
    return burger


def make_burger(burger, *funcs):
    for func in funcs:
        burger = func(burger)
    return burger


custom_burger = make_burger({}, add_bacon, add_double_meal, remove_onion)
print(custom_burger)
custom_burger_2 = make_burger({}, add_gluten_free_bun, remove_onion)
print(custom_burger_2)
