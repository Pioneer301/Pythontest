# -*- encoding:utf-8 -*-

def log(func):
    def wrapper(*args, **kvargs):
        print 'before calling ', func.__name__
        func(*args, **kvargs)
        print 'end calling ', func.__name__

    return wrapper


@log
def hello(name, age):
    print 'hello', name, age


if __name__ == '__main__':
    hello('nowcoder', 2)
