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
            print ("3.Я - обёртка вокруг декорируемой функции. "
                  "4.Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. "
                  "5.Я возвращаю результат работы декорируемой функции.")
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



