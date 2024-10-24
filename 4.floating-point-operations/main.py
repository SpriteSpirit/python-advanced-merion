# float vs Decimal
from math import floor, ceil
from decimal import Decimal, getcontext

print(10 / 2)
print(10 // 2)
print(int(10 / 4))
print(round(2 / 3, 2))
print(round(1 / 3, 2))


# rounding with floor and ceil
print(floor(2.5))
print(ceil(2.5))
print(floor(2.6))
print(ceil(2.6))
print(floor(2.1))
print(ceil(2.1))

e = 2.7
print(e)

pi = 3.1415
print(pi)

print(e + pi)

print(0.2 + 0.1)  # погрешность
print(0.3 == 0.2 + 0.1)  # False

# rounding with Decimal
print(2 + 1)
print(Decimal(1))
print(Decimal('0.1'))
print(Decimal('0.2'))

res = Decimal('0.1') + Decimal('0.2')
print(res)
print(float(res) == 0.3)
print(res == Decimal('0.3'))
print(res == 0.3)


def multi_div(iterations, number, divisor):
    for _ in range(iterations):
        number /= divisor
    return number


res_func = multi_div(3, 56, 2)
print(res_func)

res_func2 = multi_div(1, 50, 4)
print(res_func2)

print(765432/1_000_000)

res_func3 = multi_div(6, 765432, 10)
print(res_func3)

res_func4 = multi_div(6, 123456, 10)  # Погрешность
print(res_func4)


# Модификация функции с помощью Decimal
def multi_div(iterations, number, divisor):
    number = Decimal(number)

    for _ in range(iterations):
        number /= divisor
    return number


res_func5 = multi_div(6, 123456, 10)  # Погрешность
print(res_func5)
