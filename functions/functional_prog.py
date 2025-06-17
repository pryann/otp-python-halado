from functools import reduce

yearly_salaries = [10000, 12000, 15000, 18000, 20000, 25000]

# procedural programming


def calculate_summa_yearly_salaries(salaries):
    summa_yearly_salary = 0
    for salary in salaries:
        summa_yearly_salary += salary
    return summa_yearly_salary


print(calculate_summa_yearly_salaries(yearly_salaries))


def increase_salaries(salaries, increasePercent):
    increased_salaries = []
    for salary in salaries:
        increased_salaries.append(salary * (1 + increasePercent / 100))
    return increased_salaries


# functional programming


def fn(a):
    return a + 1


def increase_salaries_funcional(salaries, increasePercent):
    return list(map(lambda salary: salary * (1 + increasePercent / 100), salaries))


print(increase_salaries_funcional(yearly_salaries, 10))

# legyen egy olyan függvény, ami visszaadja a paraméterként kapott string list nagybetűs változatát
# a visszatérési érték is list legyen
str_list = ["hello", "world", "python", "functional", "programming"]


# def convert_to_upper(text):
#     return text.upper()


def convert_to_uppercase(text_list):
    return list(map(lambda text: text.upper(), text_list))


print(convert_to_uppercase(str_list))

# uppercase_list = [text.upper() for text in str_list]
# uppercase_list = list(map(lambda text: text.upper(), str_list))

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_number = list(filter(lambda num: num % 2 != 0, num_list))
even_number = list(filter(lambda num: num % 2 == 0, num_list))
print(odd_number)
print(even_number)

mixed_list = [
    1,
    "hello",
    2.5,
    "world",
    3,
    "python",
    4.0,
    True,
    "functional",
    5,
    [1, 2, 3],
    (1, 2),
]

int_list = list(filter(lambda item: type(item) is int, mixed_list))
print(int_list)

sum_num_list = reduce(lambda x, y: x + y, [], 0)
print(sum_num_list)

# vegyünk a számok négyzetét
# szűrjük ki a 20-nál kisebbeket
# mennyi a maradék összege

result = reduce(
    lambda x, y: x + y, filter(lambda num: num >= 20, map(lambda x: x**2, num_list)), 0
)
print(result)


result_pythonian = sum([num_s for num in num_list if (num_s := num**2) >= 20])
print(result_pythonian)
