"""
Лямбда-функции
Примеры map и filters
Аналоги comprehensions
Сравнение производительности решений
"""
from timeit import timeit
from operator import add

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

# Применить к каждому числу в списке квадрат
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


# Время выполнения функции power 1.1439873999916017
print(timeit(
    stmt="[power(a, b) for a, b in zip(some_numbers, some_powers)]",
    globals={
        "power": power,
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# Время выполнения функции power через map 0.8382745000126306
print(timeit(
    stmt="list(map(power, some_numbers, some_powers))",
    globals={
        "power": power,
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# Более практичное использование list comprehension время выполнения 0.7459907000011299
print(timeit(
    stmt="[a ** b for a, b in zip(some_numbers, some_powers)]",
    globals={
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# Работа map c lambda время выполнения 0.836663399997633
print(timeit(
    stmt="list(map(lambda x, y: x ** y, some_numbers, some_powers))",
    globals={
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# Использование map вместе с lambda и comprehension
# Работа map c функцией pow время выполнения 0.46844110000529326 !!
print(timeit(
    stmt="list(map(pow, some_numbers, some_powers))",
    globals={
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# Пример того, что встроенные функции работают быстрее. Время выполнения: 0.3382809000031557
print(timeit(
    stmt="list(map(add, some_numbers, some_powers))",
    globals={
        "add": add,
        "some_numbers": some_numbers,
        "some_powers": some_powers,
    },
))

# Время обработки методов строк
print("abC".title())

names = [
    'sarah kHOnor',
    'KatE',
    'sAM wHIte',
    'joHN',
]

# более производительный вариант
names_pretty = [
    name.title()
    for name in names
]

print(names_pretty)

# менее производительный вариант
names_pretty = list(
    map(lambda s: s.title(), names)
)

print(names_pretty)

# пример использования функции класса
print(str.title("wOrLd"))

# более быстрый вариант
names_pretty = list(
    map(str.title, names)
)

print(names_pretty)

# время выполнения: 0.5781505999912042
print(timeit(
    stmt="[name.title() for name in names]",
    globals={
        "names": names,
    },
    number=1_000_000,
))

# время выполнения: 0.7647843000013381
print(timeit(
    stmt="list(map(lambda s: s.title(), names))",
    globals={
        "names": names,
    },
    number=1_000_000,
))

# время выполнения: 0.5489717999880668
print(timeit(
    stmt="list(map(str.title, names))",
    globals={
        "names": names,
    },
    number=1_000_000,
))

# filter()

# Использование в циклах
for num in filter(lambda n: n >= 0, some_numbers):
    print(num)

# Использование с list
not_negative = list(filter(lambda n: n >= 0, some_numbers))
print(not_negative)

# Использование с list comprehensions
not_negative = [num for num in some_numbers if num >= 0]
print(not_negative)


# Использование с функцией
def is_not_negative(n):
    return n >= 0


not_negative = list(filter(is_not_negative, some_numbers))
print(not_negative)


# время выполнения: 0.5922538000158966
print(timeit(
    stmt="list(filter(lambda n: n >= 0, some_numbers))",
    globals={
        "some_numbers": some_numbers,
    },
    number=1_000_000,
))

# время выполнения: 0.37028119998285547
print(timeit(
    stmt="[num for num in some_numbers if num >= 0]",
    globals={
        "some_numbers": some_numbers,
    },
    number=1_000_000,
))

# время выполнения: 0.556725499976892
print(timeit(
    stmt="list(filter(is_not_negative, some_numbers))",
    globals={
        "is_not_negative": is_not_negative,
        "some_numbers": some_numbers,
    },
    number=1_000_000,
))

numbers = range(1, 11)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

odds = [n for n in numbers if n % 2]
print(odds)

odds = [n for n in numbers if n % 2 != 0]
print(odds)

# время выполнения: 0.6007358999922872
print(timeit(
    stmt="[n for n in numbers if n % 2 == 0]",
    globals={
        "numbers": numbers,
    },
    number=1_000_000,
))

# время выполнения: 0.5766186999971978
print(timeit(
    stmt="[n for n in numbers if n % 2]",
    globals={
        "numbers": numbers,
    },
    number=1_000_000,
))

# время выполнения: 0.6115087000071071
print(timeit(
    stmt="[n for n in numbers if n % 2 != 0]",
    globals={
        "numbers": numbers,
    },
    number=1_000_000,
))

