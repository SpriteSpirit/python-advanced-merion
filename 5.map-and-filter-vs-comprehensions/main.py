"""
Лямбда-функции
Примеры map и filters
Аналоги comprehensions
Сравнение производительности решений
"""
from timeit import timeit

# map - инструмент, который позволяет пройти по коллекции и применить на нее функцию
# map(func, *iterables) --> map object
print(map.__doc__)

some_numbers = [1, 2, 3, 4, 0, -3, -2, -1]

# простой вариант преобразования чисел по модулю
abs_nums = []

for num in some_numbers:
    abs_nums.append(abs(num))

print(abs_nums)

# применить к каждому числу в списке abs(), возвращающую значение по модулю
print(list(map(abs, some_numbers)))

# генератор возвращает числа по модулю
for num in map(abs, some_numbers):
    print(num)

# преобразование строки
print(list(map(str.upper, 'Hello')))

# list comprehension
abs_nums = [abs(num) for num in some_numbers]
print(abs_nums)


def square(n):
    return n ** 2


print(square(4))

# применить к каждому числу в списке квадрат
for num in some_numbers:
    if num == some_numbers[-1]:
        print(square(num), end='\n')
    else:
        print(square(num), end=' ')

for s in map(square, some_numbers):
    print(s, end=' ')

squares = [square(num) for num in some_numbers]
print(f'\n{squares}')

some_powers = [100, 10, 3, 0, 4, 2, 1]
some_numbers = [1, 2, 3, 4, 0, -3, -2, -1]

for n in map(lambda x, y: x ** y, some_numbers, some_powers):
    print(n, end=' ')

# zip - проходит по элементам 2х коллекций

for n, p in zip(some_numbers, some_powers):
    print(n, '^', p)

print(list(zip(some_numbers, some_powers)))

nums_powers = [
    x ** y
    for x, y in zip(some_numbers, some_powers)
]

print(nums_powers)


# Сравнение производительности решений
# 0.047416400018846616
print(timeit(
    stmt="lambda x, y: x ** y",
))


def power(a, b):
    return a ** b


# время выполнения функции power 1.1439873999916017
print(timeit(
    stmt="[power(a, b) for a, b in zip(some_numbers, some_powers)]",
    globals={
        "power": power,
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# время выполнения функции power через map 0.8382745000126306
print(timeit(
    stmt="list(map(power, some_numbers, some_powers))",
    globals={
        "power": power,
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))


# более практичное использование list comprehension время выполнения 0.7459907000011299
print(timeit(
    stmt="[a ** b for a, b in zip(some_numbers, some_powers)]",
    globals={
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# работа map c lambda время выполнения 0.836663399997633
print(timeit(
    stmt="list(map(lambda x, y: x ** y, some_numbers, some_powers))",
    globals={
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

