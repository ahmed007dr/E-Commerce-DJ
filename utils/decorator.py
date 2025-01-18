
def decorator(func):
    def wrapper():
        print('first')
        func() #excute
        print('last')

    return wrapper


@decorator
def x():
    print('hello')
x()
