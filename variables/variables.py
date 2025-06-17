# standard assignment
# i prefer this style
a = 10
b = 20

# chained assignment
x = y = z = 30
print(x, y, z)

# multiple assignment
i, j = 40, 50

print(i, j)

# when use multiple assignment

nums = [34, 545, 45, 40, 778, 90]


def linear_sort(sortable_list):
    for i in range(len(sortable_list)):
        for j in range(i + 1, len(sortable_list)):
            if sortable_list[i] > sortable_list[j]:
                # tmp = sortable_list[i]
                # sortable_list[i] = sortable_list[j]
                # sortable_list[j] = tmp
                sortable_list[i], sortable_list[j] = sortable_list[j], sortable_list[i]
    return sortable_list


print(linear_sort(nums))
print(nums)
