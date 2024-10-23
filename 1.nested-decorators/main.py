from functools import cache
from functools import wraps


# @cache
# def fib(n):
#     """
#      Создать функцию для вычисления последовательности Фибоначчи
#      0 1 1 2 3 5 8 13 21
#     """
#
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)


# print([fib(n) for n in range(11)])
# print(fib(55))
# fib = cache(fib)  # кэширование - позволяет избежать лишних вычислений или обращений


# 1.1. Создать декоратор для кеширования результатов вызова функции
def cached(func):
    """
    Кеширует результаты вызова функции

    :param func: функция, которую нужно кэшировать
    :return: функцию из декоратора
    """
    results = {}

    @wraps(func)
    def wrapped(n: int):
        """
        Запоминает результат вызова функции и возвращает его при повторном вызове

        :return: результат функции
        """
        if n not in results:
            # print(f"Кеширование вызова функции {func.__name__} с аргументом {n}")
            results[n] = func(n)
        return results[n]

    return wrapped


# 1.2. Применить декоратор к функции fib
# @cached
# def fib(n):
#     """
#      Создать функцию для вычисления последовательности Фибоначчи
#      0 1 1 2 3 5 8 13 21
#     """
#
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)


# print(fib(55))
# print([fib(n) for n in range(10, 20)])

"""
Декоратор, который покажет в каком порядке разворачиваются несколько декораторов
trace() показывает какие вызовы были сделаны над этой функцией
"""


def trace(func):
    """
    Декоратор для отслеживания вызовов функции

    :param func: функция, которую нужно отслеживать
    :return: функцию из декоратора
    """
    sep = "="
    func.calls = 0

    @wraps(func)
    def wrapper(*a, **kw):
        func.calls += 1
        print(sep * func.calls, f"-> {func.__name__}(*{a}, **{kw})")
        try:
            return func(*a, **kw)
        finally:
            print(sep * func.calls, f"<- {func.__name__}(*{a}, **{kw})")
            func.calls -= 1

    return wrapper


@trace
@cache
def fib(n):
    """
     Функция для вычисления последовательности Фибоначчи
     0 1 1 2 3 5 8 13 21
    """

    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


# print(fib(3))
# print(fib(5))
# print(fib(10))
# print(fib(12))
# print(fib(12))

"""
Порядок декораторов:
В первом случае декораторы применены в порядке @trace @cache, 
что означает, что fib сначала кэшируется, а затем отслеживается.

Во втором случае порядок обратный: @cache @trace, что означает, 
что fib сначала отслеживается, а затем кэшируется.

Пример для понимания:
Первый случай (@trace @cache):

@trace
@cache
def fib(n):
    ...
    
Здесь:
cache кэширует результаты.
trace выводит только новые вызовы, потому что повторные вызовы возвращают кэшированный результат.

Второй случай (@cache @trace):

@cache
@trace
def fib(n):
    ...
    
Здесь:
trace отслеживает каждый вызов.
cache кэширует результаты, но это не влияет на то, что trace уже отследил вызов.

Резюме:
Если нужно увидеть все вызовы функции, включая повторные, то применяется trace до cache.
Если нужно увидеть только уникальные вызовы, то применяется cache до trace.
"""


def trace(_func=None, *, sep="="):
    """
    Декоратор, который генерирует декоратор

    :param _func: передается позиционно
    :param sep: декоратор (передается именованно)
    :return: функцию из декоратора
    :param *: функция не принимает ничего, кроме именованных аргументов после позиционного
    """

    def decorator(func):
        """
        Декоратор для отслеживания вызовов функции

        :param func: функция, которую нужно отслеживать
        :return: функцию из декоратора
        """

        func.calls = 0

        @wraps(func)
        def wrapper(*a, **kw):
            func.calls += 1
            print(sep * func.calls, f"-> {func.__name__}(*{a}, **{kw})")
            try:
                return func(*a, **kw)
            finally:
                print(sep * func.calls, f"<- {func.__name__}(*{a}, **{kw})")
                func.calls -= 1

        return wrapper

    # проверка ввода параметра
    # if isinstance(sep, str):
    #     return decorator
    #
    # _func = sep
    # sep = "="
    # return decorator(_func)

    if _func is not None:
        return decorator(_func)
    return decorator


@trace(sep='+')
@cache
def fib(n):
    """
     Функция для вычисления последовательности Фибоначчи
     0 1 1 2 3 5 8 13 21
    """

    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(3))
