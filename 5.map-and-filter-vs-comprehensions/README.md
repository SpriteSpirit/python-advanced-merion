## Функция map 
- применяется к каждому элементу итерируемого объекта (например, списка) указанную функцию и возвращает
итератор с результатами.

### Синтаксис:
```python
map(function, iterable, ...)
```
```text
function: функция, которая будет применена к каждому элементу.
iterable: один или несколько итерируемых объектов.
```


#### Пример:
```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Вывод: [1, 4, 9, 16]
```

## Функция zip 
- берёт несколько итерируемых объектов и возвращает итератор кортежей,
где каждый кортеж содержит элементы с одинаковыми индексами из всех итерируемых объектов.

### Синтаксис:
```python
zip(iterable1, iterable2, ...)
```
#### Пример:
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))  # Вывод: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```
## Метод ' '.join() 
- используется для объединения элементов списка (или любого итерируемого объекта)
в одну строку, при этом между элементами вставляется указанный разделитель.

```python
some_words = ['Hello', 'Hi', 'Welcome', 'go']
some_words_too = ['world!', 'friends!', 'and', 'away!']

print(' '.join(map(lambda x, y: f'{x} {y}', some_words, some_words_too)))
```
## Модуль timeit 
**Используется для измерения времени выполнения определенного выражения**

**stmt="lambda x, y: x ** y"**
- это выражение, которое будет выполнено и замерено по времени. В данном случае это лямбда-функция, которая возводит число x в степень y.


**globals={"power": lambda x, y: x ** y}**
- это словарь, содержащий глобальные переменные, которые будут доступны во время выполнения выражения. В данном случае, здесь определена лямбда-функция power, которая также возводит число x в степень y.
```python

from timeit import timeit

some_powers = [100, 10, 3, 0, 4, 2, 1]
some_numbers = [1, 2, 3, 4, 0, -3, -2, -1]

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
```
## Функция filter() 
- используется для фильтрации элементов из итерируемого объекта (такого как список, кортеж или строка) на основе определенного условия.

**Функция filter() принимает два аргумента:**
```text
function: функция, которая будет применена к каждому элементу в последовательности.
iterable: последовательность (например, список, кортеж, набор), элементы которой будут обработаны функцией.

return: итератор, который содержит только те элементы из исходного итерируемого объекта, для которых функция-условие вернула True.
```
### В общем случае функция filter() работает следующим образом:

1. Итератор filter() начинает обход последовательности iterable.
2. Для каждого элемента в последовательности функция function вызывается с этим элементом в качестве аргумента.
3. Если функция function возвращает значение True, элемент включается в результат.
4. Если функция function возвращает значение False, элемент игнорируется

**Пример использования функции filter():**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # [2, 4, 6, 8]
```


**Функция filter() также может быть использована с любыми другими функциями, а не только с лямбда-функциями. Например:**
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # [2, 4, 6, 8]
```