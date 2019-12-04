def createSpiral(n):
    if not isinstance(n, int): return []
    d = iter(range(n ** 2))
    a = r = [[[x, y] for y in range(n)] for x in range(n)]
    while a:
        for x, y in a[0]: r[x][y] = next(d) + 1
        a = list(zip(*a[1:]))[::-1]
    return r

def func_for_decorate(func_to_decorate):
    print("\n\nIn decorator\n")
    def wrapper():
        print(func_to_decorate())
        print("Out of decorator\n\n")
    return wrapper


def decorator_maker():
    print ("1.Я создаю декораторы! Я буду вызван только раз: "+"когда ты попросишь меня создать тебе декоратор.")
    def my_decorator(func):
        print ("2.Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
        def wrapped():
            print ("""3.Я - обёртка вокруг декорируемой функции. 
                4.Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. 
                5.Я возвращаю результат работы декорируемой функции.""")
            return func()
        print("6.Я возвращаю обёрнутую функцию.")

        return wrapped
    print ("7.Я возвращаю декоратор.")
    return my_decorator


new_decorator = decorator_maker()
print('-'*10)
def decorated_function():
    print("I decorate function")

decorated_function = new_decorator(decorated_function)

decorated_function()


print('*'*12)

@decorator_maker()
def some_func():
    print("I some decorated function")
some_func()


print('-*-'*12)

def decorator_create():
    print("1.This function create decorator.")
    
    def make_decorator(func):
        print("3.This function is decorator")

        def wrapper():
            print("5.This is wrapper for our function")
            func()
            print("7.End of wrapper function")

        print("4.End decorator")
        return wrapper
    print("2.REturn decorator")
    return make_decorator

@decorator_create()
def myfunc():
    print("6.This is my function")

myfunc()

print('-*-'*12)
"""
! Create decorator with arguments
"""

def make_decorators_with_arg(decorator_arg1, decorator_arg2):
    print("I'm creator decorator and I use this arg {}, {}".format(decorator_arg1, decorator_arg2))
    def decorator(func):
        print("I'm decorator and I can see arg from creator me {}, {}".format(decorator_arg1, decorator_arg2))
        def wrapper(arg_func):
            print("I can see all arg")
            func(arg_func)
            print("End")
        return wrapper
    return decorator

@make_decorators_with_arg("arg_1","arg_2")
def my_func_2(arg):
    print("My arg is {}".format(arg))

my_func_2("My arg")

