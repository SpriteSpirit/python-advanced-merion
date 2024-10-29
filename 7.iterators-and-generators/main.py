name = 'Angelina'
print('Hi', name)

# пример ручной итерации
print('Hi', name)
print('Hi', name)
print('Hi', name)

# пример цикличной итерации
times = 0

while times < 5:
    print('Hi', name)
    times += 1

times = 0

# изменить строковое значение проще в цикличной итерации, чем в построчной
while times < 5:
    print('Hello', name)
    times += 1

# коллекции
numbers = [1, 2, 3]

# numbers возвращает итератор
# мы идем не по списку, а по итератору, который идет по списку
for num in numbers:
    print(num)

data = {
    'foo': 'bar',
    'spam': 'eggs',
    '1': 'eggs',
    '2': 'eggs',
    '3': 'eggs',
    '4': 'eggs',
    '5': 'eggs',
}

# итератор следит за структурой
'''
Изменение размера словаря (data), при удалении элементов 
из него во время итерации по его ключам
'''
for key in data:
    # print(data.pop(key))
    pass

for i in range(10_000):
    print(i)

    if i > 7:
        break

# Различия генераторов от итераторов
r = range(7)
print(r)

for i in r:
    print(i)

    if i > 3:
        break

# r создает новый итератор, когда мы входим в цикл
# r - объект, который работает, как итератор и создает
# значения на ходу и в каждом новом цикле он будет идти сначала.
# сам r - не итератор, он только создает итератор
# итератор следит, где находимся (какой элемент) и возвращать элемент
for i in r:
    print(i)

# падает ошибкой подтверждая, что r не итератор
# next(r)

# map - генератор:
g = map(lambda n: n * n, range(8))

for i in g:
    print(f'1{i=}')

    if i > 6:
        break
# можно обратиться к следующему элементу g - генератора
print(f'{next(g)=}')

for i in g:
    print(f'2{i=}')

# генератор - частный случай итератора
# генераторы работают как итераторы, но не каждый генератор - это любой итератор
# генератор "иссяк"
for i in g:
    print(f'3{i=}')

file = 'file.txt'

# создание файла
# with open(file, 'w+', encoding='utf-8') as file:
#     file.writelines([
#         f'line {i}\n'
#         for i in range(1, 101)
#     ])

with open(file, 'r', encoding='utf-8') as file:
    for line in file:
        print(repr(line))

        if '7' in line:
            break
    print('one more line')
    print(repr(next(file)))

# генератор можно использовать только один раз
# итераторы и генераторы помогают обходить коллекции,
# зная только текущий элемент, тем самым помогая экономить ресурсы
