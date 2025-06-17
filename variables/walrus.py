yearly_list = [10000, 12000, 15000, 18000, 20000, 25000]

# version A
# yearly_salary_statistics = {
#     "count": len(yearly_list),
#     "summa": sum(yearly_list),
#     "average": sum(yearly_list) / len(yearly_list),
# }

# version B
# summa_yearly_salary = sum(yearly_list)
# count_yearly_salary = len(yearly_list)
# yearly_salary_statistics = {
#     "count": count_yearly_salary,
#     "summa": summa_yearly_salary,
#     "average": summa_yearly_salary / count_yearly_salary,
# }

# versius C
yearly_salary_statistics = {
    "count": (count_yearly_salary := len(yearly_list)),
    "summa": (summa_yearly_salary := sum(yearly_list)),
    "average": summa_yearly_salary / count_yearly_salary,
}

print(yearly_salary_statistics)
print(count_yearly_salary)

print(x := 3)
# x = 3
# print(x)

int_tuple = (1,)
print(type(int_tuple))
