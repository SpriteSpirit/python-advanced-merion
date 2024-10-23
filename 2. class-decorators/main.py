# Классы-декораторы
# Декораторы классов

# декоратор автоматически генерирует методы, такие как __init__, __repr__, и другие, для класса.
from dataclasses import dataclass

"""
декоратор автоматически создает методы __init__, __repr__, __eq__ и другие. 
Опция slots=True указывает Python использовать __slots__ вместо __dict__ для хранения атрибутов. 
Это оптимизирует использование памяти, но ограничивает возможность динамического добавления атрибутов.
"""


@dataclass(slots=True)
class User:
    """Класс пользователь с id и именем."""
    id: int
    username: str


user = User(id=1, username="John")

print(user)  # User(id=1, username='John')

"""
User.__slots__ выводит список слотов, которые определены для класса User. 
Слоты - это специальные атрибуты, которые хранятся в памяти более эффективно, чем словарь __dict__. 
В этом случае, слоты - это ('id', 'username').
"""
print(User.__slots__)

"""
User.mro() выводит список классов, которые наследуются классом User. 
Метод mro() возвращает список классов в порядке, в котором они будут поисках атрибутов. 
В этом случае, список - это (<class '__main__.User'>, <class 'object'>).
"""
print(User.mro())

"""
User.__dataclass_params__ выводит параметры класса данных, которые были переданы декоратору @dataclass. 
В этом случае, параметры - это {'slots': True}.
"""
print(User.__dataclass_params__)

"""
выводит строковое представление объекта user с помощью метода __repr__. Результат аналогичен выводу print(user).
"""
print(repr(user))


"""
MRO расшифровывается как Method Resolution Order (Порядок разрешения методов). 
Это термин в Python, который описывает порядок, в котором Python ищет методы и атрибуты в иерархии классов 
при их вызове или доступе.
"""


class A:
    def metodo(self):
        print("A.metodo")


class B(A):
    def metodo(self):
        print("B.metodo")


class C(A):
    def metodo(self):
        print("C.metodo")


class D(B, C):
    pass


print(D.mro())


# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

'''
Пояснение:
Python сначала проверяет D, затем B, затем C, затем A и, наконец, object.
Если метод или атрибут не найден в D, Python ищет его в B, затем в C, и так далее.
Зачем это нужно:
Предсказуемость: MRO обеспечивает предсказуемое поведение при наследовании, особенно в сложных иерархиях классов.
Избежание конфликтов: MRO помогает разрешать конфликты, когда методы переопределяются в разных базовых классах.
'''

# Простой декоратор для регистрации моделей
# Создается пустой словарь registry для хранения классов.
registry = {}


def register_model(cls):
    """
    Декоратор для регистрации моделей.
    Принимает класс и добавляет его в словарь registry, под ключом, равным имени класса (cls.__name__).
    Добавляет ссылку на registry как атрибут класса под именем __models_registry__
    :param cls: класс для регистрации
    :return: возвращает класс, позволяя использовать декоратор.
    """

    registry[cls.__name__] = cls
    cls.__models_registry__ = registry

    return cls


print(registry)


@register_model
class Post:
    pass


print(registry)


@register_model
class Comment:
    pass


print(Comment.__models_registry__)


# Класс для управления регистром моделей
class ModelsRegistry:
    """
    Класс для хранения регистра моделей.
    Позволяет получать доступ к регистру моделей и выполнять операции с ними.
    Атрибут _registry нужен  для хранения классов.
    """
    def __init__(self):
        self._registry = {}

    def register(self, decorated_class):
        """
        Метод registrer работает аналогично register_model, но использует внутренний словарь _registry.
        :param decorated_class:
        :return:
        """
        self._registry[decorated_class.__name__] = decorated_class
        decorated_class.__models_registry__ = self._registry

        return decorated_class


models_registry = ModelsRegistry()
print(models_registry._registry)


@models_registry.register
class Client:
    pass


print(models_registry._registry)


@models_registry.register
class Manager:
    pass


print(models_registry._registry)

"""
Декораторы для классов: В Python декораторы классов используются для изменения или расширения классов 
без изменения их определения. 
Здесь они используются для автоматической регистрации классов в словаре или в атрибуте объекта.
***
Регистрация моделей: Это паттерн, который позволяет централизованно управлять классами моделей, 
что может быть полезно для фреймворков или систем, где необходимо динамически работать с различными типами моделей.
***
Использование атрибутов класса: Добавление атрибутов к классам (как __models_registry__) позволяет 
классам иметь доступ к общему регистру, что может быть полезно для метапрограммирования или для создания гибких систем.
"""
