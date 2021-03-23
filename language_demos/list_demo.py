

# car1 = (1, "Ford", "Fusion Hybrid", "blue", 45000)
# car2 = (2, "Tesla", "S", "red", 150000)

# cars = [car1, car2]

nums = [1, 2, 3, 4, 5]

# very imperative stucture
# for (int x=0; x<nums.length; x++) {
#     print(nums[x])
# }

# imperative code - very weak semantic meaning
# counter = 0
# while counter < len(nums):
#     print(nums[counter])
#     counter = counter + 1

# declarative code - very strong semantic meaning
# for num in nums:
#     print(num)

# relatively imperative way of performing this operation
# double_nums = []

# for num in nums:
#     double_nums.append(num * 2)


def double(n):
    print("called double: " + str(n))
    return n * 2


# def my_map(transform_fn, items):
#     new_items = []
#     for item in items:
#         new_items.append(transform_fn(item))
#     return new_items

def my_map(transform_fn, items):
    for item in items:
        print("transform item: " + str(item))
        yield transform_fn(item)


# double_nums = map(double, nums)
# double_nums = list(map(lambda x: x * 2, nums))
double_nums = my_map(double, nums)

# list comprehension
# double_nums = [x * 2 for x in nums]

# print(nums)
print(double_nums)

for num in double_nums:
    print(num)
    if num > 5:
        break

# for num in double_nums:
#     print(num)
#     if num > 5:
#         break


