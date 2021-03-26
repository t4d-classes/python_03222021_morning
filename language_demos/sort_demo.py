
from random import randint


def gen_name(name_len=4):
    return "".join([chr(randint(65, 90)) for _ in range(name_len)])


random_dicts = [{"id": randint(1, 1000), "name": gen_name(5)}
                for _ in range(100)]

# random_dicts.sort(key=lambda x: x["name"])

sorted_random_dicts = sorted(random_dicts, key=lambda x: x["name"])

print(random_dicts)
print(sorted_random_dicts)


# random_nums = [randint(1, 1000) for _ in range(100)]

# # print(random_nums)

# # random_nums.sort()
# # print(random_nums)

# sorted_random_nums = sorted(random_nums)

# print(random_nums)
# print(sorted_random_nums)
