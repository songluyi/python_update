#厉害！
import functools

def log(*pram):
    if callable(pram[0]):
        print(pram[0])
        @functools.wraps(pram[0])
        def wrapper(*args, **kw):
            print('begin call')
            print('call %s():' % pram[0].__name__)
            pram[0](*args, **kw)
            print('end call')
        return wrapper

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            print('%s %s():' % (pram[0], func.__name__))
            func(*args, **kw)
            print('end call')
        return wrapper
    return decorator

@log
def now():
    print('2016-08-27')

now()

@log('execute')
def now():
    print('2016-08-27')
now()