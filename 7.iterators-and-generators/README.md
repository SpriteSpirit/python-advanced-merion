# Итераторы и генераторы

> - что такое итератор в Python и когда с ним сталкиваются
>- что такое генератор и зачем он нужен
>- чтение файла

## Итераторы

> - Это объекты, которые реализуют методы `__iter__()` и `__next__()`
>- Позволяют проходить по последовательности элементов
>- Хранят состояние о текущей позиции
>- Выбрасывают `StopIteration`, когда элементы закончились

### Пример:

```python
# Пример итератора
numbers = [1, 2, 3]
iterator = iter(numbers)  # получаем итератор
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration
```

## Генераторы

> - Это особый вид итераторов
>- Создаются с помощью функций с `yield` или генераторных выражений
>- Вычисляют значения "на лету", не храня всю последовательность в памяти
>- Могут быть использованы только один раз
>- После исчерпания не могут быть использованы повторно

### Пример:

```python
# Пример генератора-функции
def number_generator(n):
    for i in range(n):
        yield i


gen = number_generator(3)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# print(next(gen))  # StopIteration

# Пример генераторного выражения
squares = (x * x for x in range(3))
```

## Ключевые различия:

> 1. Генератор - это подвид итератора с дополнительными возможностями
>2. Генераторы создают значения "на лету", экономя память
>3. Генераторы можно использовать только один раз, тогда как некоторые итераторы (например, `range`) можно использовать
    многократно

### Пример:

```python
# range создает новый итератор при каждом использовании
r = range(3)
for i in r:
    print(i)
for i in r:  # можно использовать снова
    print(i)

# генератор можно использовать только один раз
g = (x for x in range(3))
for i in g:
    print(i)
for i in g:  # второй раз ничего не выведет
    print(i)
```

## Применение:

> Итераторы идеально подходят для обхода элементов любых итерируемых объектов, в то время как генераторы лучше подходят
> для создания итераторов, которые вычисляют значения по мере необходимости, особенно для потенциально бесконечных
> последовательностей.

## Создание:

> Итераторы требуют реализации методов `__iter__()` и `__next__()`, в то время как генераторы создаются автоматически с
> использованием функций с операторами yield или генераторных выражений.

## Удобство:

> Генераторы обеспечивают более удобный и компактный способ реализации итераторов, поскольку не требуют явного
> определения классов с методами `__iter__()` и `__next__()`
>

## Дополнительные примеры:

```python
# 1. map() создает генератор 
g = map(lambda n: n * n, range(8))
```

```python
# 2. файловый объект является итератором
file = 'file.txt'

with open(file, 'r', encoding='utf-8') as file:
    for line in file:
        print(repr(line))

        if '7' in line:
            break
    print('one more line')
    print(repr(next(file)))
```

```python
# 3. range() создает объект, который при итерации создает новый итератор
# Создаем объект range
r = range(5)
print(f"Объект range: {r}")  # range(0, 5)

# Получаем итератор из range
iterator1 = iter(r)
print(f"Первый итератор: {iterator1}")

# Получаем второй итератор из того же range
iterator2 = iter(r)
print(f"Второй итератор: {iterator2}")

# Доказываем, что это разные итераторы
print("\nРабота с первым итератором:")
print(next(iterator1))  # 0
print(next(iterator1))  # 1

print("\nРабота со вторым итератором:")
print(next(iterator2))  # 0 (начинает сначала!)
print(next(iterator2))  # 1

print("\nПродолжаем работу с первым итератором:")
print(next(iterator1))  # 2 (продолжает с того места, где остановился)

# Можно также использовать в циклах многократно
print("\nПервый проход по range:")
for i in r:
    print(i, end=' ')  # 0 1 2 3 4

print("\nВторой проход по range:")
for i in r:
    print(i, end=' ')  # 0 1 2 3 4

# Для сравнения - генератор:
print("\n\nРабота с генератором:")
g = (x for x in range(5))  # создаем генератор

print("Первый проход по генератору:")
for i in g:
    print(i, end=' ')  # 0 1 2 3 4

print("\nВторой проход по генератору:")
for i in g:
    print(i, end=' ')  # ничего не выведет, так как генератор уже исчерпан
```

> Генераторы являются специальным случаем итераторов с более простым синтаксисом для создания и использования,
> обеспечивающим ленивую обработку данных. 
> 
>Итераторы — это более общий термин для объектов, поддерживающих итерационный
> протокол. Оба они играют ключевую роль в эффективной обработке коллекций и потоков данных в Python.

> **Основное преимущество генераторов и итераторов - это экономия памяти, так как они не требуют хранения всей**
> **последовательности в памяти одновременно.**