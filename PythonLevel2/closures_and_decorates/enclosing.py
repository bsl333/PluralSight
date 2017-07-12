message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # nonlocal message
        message = 'local'

    print('enclosing message: ', message)  # enclosing
    local()

    print('enclosing message: ', message)  # enclosing

print('enclosing message: ', message)  # global
enclosing()
print('enclosing message: ', message)  # global
