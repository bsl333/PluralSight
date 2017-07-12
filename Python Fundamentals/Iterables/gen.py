
def gen123():
    yield 1
    yield 2
    yield 3

def take(count, iterable):
    """
    Takes items form the front of an iterable

    :param count: max numbers of items to retrieve
    :param iterable: the source series

    Yield:
        at most 'count' items from 'iterable'
    """

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


run_take()
it = gen123()
for i in it:
    print(i)

