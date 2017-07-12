def outer():
    x = 3

    def inner(y):
        return x + y

    return inner

i = outer()

print(i(10))

