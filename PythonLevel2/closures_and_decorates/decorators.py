# DECORATOR EXAMPLE WITH A FUNCTION #
def my_dec(func):
    def wrap(*args, **kwargs):
        x = func(*args, **kwargs)
        print(kwargs)
        print(args)
        return print("the result of {} is: {} and the square is: {}".format(func.__name__, x, x*x))

    return wrap


@my_dec
def my_func(x, y, *args, **kwargs):
    return x + y


my_func(1, 10, 3, 5, pow=2)
# END #


# DECORATOR EXAMPLE WITH A CLASS #
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(self.count)
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('hello {}'.format(name))

hello('Branden')
hello('Jock')
print(hello.count) # takes on the attribute of the class


# Validating Args with Decorators:
# checn_non_negative is not a decorator; what's inside it is.
def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('arg {} must be non-neg'.format(index))
            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return value * size


create_list('branden', 3)
# create_list('b', -3)



