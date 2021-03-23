import itertools

# 0 1 1 2 3 5 (num 1) 8 (num 2) 13 (next num)


def fibonacci():

    num_1 = 0
    num_2 = 1

    yield num_1, num_1

    while True:

        next_num = num_1 + num_2
        yield num_2, next_num
        num_1 = num_2
        num_2 = next_num


fib_gen = fibonacci()

# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))
# print(next(fib_gen))

# print(fib_gen)

for prev_num, num in itertools.islice(fib_gen, 2000, 2020):
    print(hex(num))
    # print(num, float(num) / float(prev_num) if prev_num > 0 else 'no ratio')
