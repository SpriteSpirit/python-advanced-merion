from sys import getrecursionlimit, setrecursionlimit
from dataclasses import dataclass, field
from typing import Any
from functools import wraps, reduce
from operator import mul

stack = []

stack.append("apple")
stack.append("banana")
stack.append("orange")

print(stack)

print(stack.pop())


def factorial(n):
    if n <= 2:
        return n
    return n * factorial(n - 1)


print(f'{getrecursionlimit()=}')
print(factorial(1000))
setrecursionlimit(500)
print(factorial(500))
setrecursionlimit(5000)
# print(factorial(5000))  # Exceeds the limit (4300)
setrecursionlimit(100)
print(f'{getrecursionlimit()=}')


def fac(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(f'{getrecursionlimit()=}')
print(f'{fac(10)=}')
print(f'{fac(110)=}')


# функция для демонстрации хвостовой рекурсии
def factorial(n, accumulator=1):
    """
    Стандартная рекурсивная функция для вычисления факториала.
    Здесь используется аргумент accumulator, который накапливает результат,
    что делает функцию хвостовой (последним действием функции является
    возврат результата вызова самой себя).
    :param n: Факториал числа
    :param accumulator: Аккумулятор - накапливает результат
    :return: Хвостовой вызов (последняя операция в функции)
    """
    if n <= 2:
        return n * accumulator
    return factorial(n - 1, accumulator=accumulator * n)


# print(factorial(10))


@dataclass
class TailCall:
    """
    Класс для проверки какой вызов нужно сделать: рекурсивный или итерационный
    """
    args: tuple[Any, ...] = field(default_factory=tuple)
    kwargs: dict[str, Any] = field(default_factory=dict)


def tail_recursion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = TailCall(args, kwargs)

        while isinstance(result, TailCall):
            result = func(*result.args, **result.kwargs)
        return result

    return wrapper


def tail(*args, **kwargs):
    return TailCall(args, kwargs)


# использование декоратора tail_recursion для проверки хвостовой рекурсии
@tail_recursion
def factorial(n, accumulator=1):
    if n <= 2:
        return n * accumulator
    return tail(n - 1, accumulator=accumulator * n)


print(f'{factorial(100)=}')

# факториал от 6
print(reduce(lambda a, b: a * b, range(1, 4)))

# факториал от 10
print(reduce(lambda a, b: a * b, range(1, 11)))

# более быстрый и короткий вариант записи для вычисления факториала от 10
print(reduce(mul, range(1, 11)))
