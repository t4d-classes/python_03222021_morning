

some_var = None
print(type(some_var))

some_var = 2
print(type(some_var))

some_var_b = 3.0
print(type(some_var_b))

# print(some_var + some_var_b)
# # print("some var: " + str(some_var))

some_var = "hello, world"
print(type(some_var))

some_var = False
print(type(some_var))

# tuple is immutable
some_var = (1, 'fun', False)
print(type(some_var))

print(some_var[1])

# lists are mutable
some_var = [1, 2, 3, 4, 5]

print(type(some_var))

some_var.append(10)
print(some_var)

some_var.remove(3)
print(some_var)


def do_it():
    print("did it")


do_it()
print(type(do_it))
