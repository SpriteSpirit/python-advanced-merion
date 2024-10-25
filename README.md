# Разбор принципов ООП, SOLID, KISS, DRY

### Оглавление:
* [ООП](#ооп)
    * [Инкапсуляция](#1-инкапсуляция)
    * [Наследование](#2-наследование)
    * [Полиморфизм](#3-полиморфизм)
    * [Абстракция](#4-абстракция)
* [SOLID](#solid)
  * [- S - Принцип единственной ответственности](#--s--)
  * [- O - Принцип открытости/закрытости](#--o---)
  * [- L - Принцип подстановки Лискова](#--l---)
  * [- I - Принцип разделения интерфейсов](#--i---)
  * [- D - Принцип инверсии зависимостей](#--d---)
* [KISS](#kiss)
* [DRY](#dry)


## ООП
 
Объектно-ориентированное программирование (ООП) основывается на нескольких ключевых принципах, которые помогают структурировать и организовать код. Рассмотрим основные принципы ООП с примерами на языке Python.

### 1. Инкапсуляция

**Описание**: Инкапсуляция — это механизм, который объединяет данные и методы, работающие с этими данными, в одном компоненте (классе) и ограничивает доступ к ним извне.

**Пример**:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватное поле

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Использование
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())  # 120
```

**Объяснение**: Поле `__balance` является приватным и не может быть изменено напрямую извне. Методы `deposit`, `withdraw` и `get_balance` предоставляют контролируемый доступ к этому полю.

### 2. Наследование

**Описание**: Наследование позволяет создавать новые классы на основе существующих, унаследовав их свойства и методы.

**Пример**:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Использование
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
```

**Объяснение**: Классы `Dog` и `Cat` наследуют свойства и методы от класса `Animal` и переопределяют метод `speak`.

### 3. Полиморфизм

**Описание**: Полиморфизм позволяет использовать объекты различных классов через общий интерфейс.

**Пример**:

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Использование
shapes = [Rectangle(2, 3), Circle(4)]
for shape in shapes:
    print(shape.area())  # 6, 50.24
```

**Объяснение**: Классы `Rectangle` и `Circle` реализуют метод `area` по-разному, но их объекты могут быть использованы через общий интерфейс `Shape`.

### 4. Абстракция

**Описание**: Абстракция позволяет скрывать сложные детали реализации и предоставлять только необходимые функции и интерфейсы.

**Пример**:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Использование
rectangle = Rectangle(2, 3)
print(rectangle.area())  # 6
```

**Объяснение**: Класс `Shape` является абстрактным и определяет интерфейс для всех фигур. Класс `Rectangle` реализует этот интерфейс, скрывая детали реализации.

Эти примеры демонстрируют основные принципы ООП и их применение на практике, что помогает создавать более структурированный, поддерживаемый и расширяемый код.


## SOLID:

### - S -
**Single Responsibility Principle (Принцип единственной ответственности)**

Предположим, у нас есть класс `User`, который хранит информацию о пользователе и отправляет ему электронную почту:
```python
class User:
     def __init__(self, name, email):
         self.name = name
         self.email = email
    
     def send_email(self, message):
         # код для отправки электронной почты
         pass
```
Проблема в том, что класс `User` имеет две ответственности: хранение информации о пользователе и отправка электронной почты. Если мы хотим изменить способ отправки электронной почты, нам придется изменить класс `User`.

Решение: создать отдельный класс `EmailSender`, который будет отвечать за отправку электронной почты:
```python
class User:
     def __init__(self, name, email):
         self.name = name
         self.email = email
    
class EmailSender:
     def send_email(self, user, message):
         # код для отправки электронной почты
         pass
```
Теперь класс `User` имеет только одну ответственность - хранение информации о пользователе.

### - O - 
**Open/Closed Principle (Принцип открытости/закрытости)**

Предположим, у нас есть класс `PaymentGateway`, который обрабатывает платежи через кредитные карты:
```python
class PaymentGateway:
     def process_payment(self, amount):
         # код для обработки платежа через кредитную карту
         pass
```
Если мы хотим добавить поддержку платежей через PayPal, нам придется изменить класс `PaymentGateway`.

Решение: создать абстрактный класс `PaymentProcessor` и конкретные классы `CreditCardProcessor` и `PayPalProcessor`, которые наследуют от него:
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
     @abstractmethod
     def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
     def process_payment(self, amount):
         # код для обработки платежа через кредитную карту
         pass

class PayPalProcessor(PaymentProcessor):
     def process_payment(self, amount):
         # код для обработки платежа через PayPal
         pass
```
Теперь мы можем добавить новые способы оплаты, не изменяя существующий код.

### - L - 
**Liskov Substitution Principle (Принцип подстановки Лискова)**

Предположим, у нас есть класс `Rectangle` и класс `Square`, который наследует от него:
```python
class Rectangle:
     def __init__(self, width, height):
         self.width = width
         self.height = height

     def area(self):
        return self.width * self.height

class Square(Rectangle):
     def __init__(self, side):
        super().__init__(side, side)
```
Проблема в том, что класс `Square` меняет поведение метода `area()`, который определен в классе `Rectangle`.

Решение: переопределить метод `area()` в классе `Square`, чтобы он возвращал правильное значение:
```python
class Square(Rectangle):
     def __init__(self, side):
        super().__init__(side, side)

     def area(self):
        return self.width ** 2
```
Теперь класс `Square` можно использовать вместо класса `Rectangle` без изменения поведения программы.

### - I - 
**Interface Segregation Principle (Принцип разделения интерфейсов)**

Предположим, у нас есть интерфейс `Printable`, который определяет методы `print()` и `scan()`:
```python
from abc import ABC, abstractmethod

class Printable(ABC):
     @abstractmethod
     def print(self):
        pass

     @abstractmethod
     def scan(self):
        pass
```
Проблема в том, что не все устройства могут выполнять оба метода. Например, принтер может печатать, но не сканировать.

Решение: разделить интерфейс `Printable` на два отдельных интерфейса `Printable` и `Scannable`:
```python
class Printable(ABC):
     @abstractmethod
     def print(self):
        pass

class Scannable(ABC):
     @abstractmethod
     def scan(self):
        pass
```
Теперь устройства могут реализовывать только те интерфейсы, которые им нужны.

### - D - 
**Dependency Inversion Principle (Принцип инверсии зависимостей)**

Предположим, у нас есть класс `UserService`, который зависит от класса `UserRepository`:
```python
class UserRepository:
     def get_user(self, id):
         # код для получения пользователя из базы данных
         pass

class UserService:
     def __init__(self):
        self.repository = UserRepository()
    
     def get_user(self, id):
        return self.repository.get_user(id)
```
Проблема в том, что класс `UserService` жестко связан с классом `UserRepository`.

Решение: ввести интерфейс `UserRepositoryInterface` и сделать класс `UserService` зависимым от него:
```python
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
     @abstractmethod
     def get_user(self, id):
        pass

class UserRepository(UserRepositoryInterface):
     def get_user(self, id):
         # код для получения пользователя из базы данных
         pass

class UserService:
     def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository
    
     def get_user(self, id):
        return self.repository.get_user(id)
```
Теперь класс `UserService` можно использовать с любым классом, который реализует интерфейс `UserRepositoryInterface`.

## KISS
(Keep It Simple, Stupid) - принцип, который гласит, что код должен быть простым и понятным. Это означает, что не следует усложнять код без необходимости, и что простое решение всегда лучше сложного.

Вот несколько примеров, которые демонстрируют принцип KISS:

**Пример 1: Сложный способ**

Предположим, у нас есть задача найти максимальное значение в списке чисел:
```python
def find_max(numbers):
     max_value = numbers[0]
     
     for num in numbers[1:]:
         if num > max_value:
            max_value = num
     return max_value
```
Этот код работает, но он слишком сложный. Мы можем упростить его, используя встроенную функцию `max()`:
```python
def find_max(numbers):
 return max(numbers)
```
**Пример 2: Неоправданная сложность**

Предположим, у нас есть задача проверить, является ли число четным или нечетным:
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```
Этот код работает, но он слишком сложный. Мы можем упростить его, используя простое выражение:
```python
def is_even(n):
    return n % 2 == 0
```
**Пример 3: Избыточная логика**

Предположим, у нас есть задача найти сумму двух чисел:
```python
def add(a, b):
    if a > 0 and b > 0:
        return a + b
    elif a < 0 and b < 0:
        return a + b
    else:
        return a + b
```
Этот код работает, но он слишком сложный. Мы можем упростить его, удалив избыточную логику:
```python
def add(a, b):
    return a + b
```
**Пример 4: Сложный интерфейс**

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
```
Этот код работает, но он слишком сложный. Мы можем упростить его, используя более простой алгоритм:
```python
class Animal:
    def make_sound(self):
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
```
Объяснение: Вместо использования пустого метода make_sound в базовом классе Animal, мы поднимаем исключение NotImplementedError, чтобы явно указать, что этот метод должен быть реализован в подклассах. Это делает код более простым и понятным.

В каждом из этих примеров мы видим, что простое решение всегда лучше сложного. Код должен быть простым, понятным и легким для чтения.


## DRY
(Don't Repeat Yourself) - принцип, который гласит, что код не должен повторяться. 
Это означает, что если есть кусок кода, который выполняет одну и ту же задачу в разных местах программы, то его следует вынести в отдельную функцию или метод, чтобы избежать дублирования кода.

Вот несколько примеров, которые демонстрируют принцип DRY:

**Пример 1: Повторяющийся код**

Предположим, у нас есть два метода, которые выполняют одну и ту же задачу - проверяют, является ли число четным или нечетным:
```python
def check_even(n):
     if n % 2 == 0:
        return "Четное"
     else:
        return "Нечетное"

def check_odd(n):
     if n % 2 == 0:
        return "Четное"
     else:
        return "Нечетное"
```
Этот код повторяется, и мы можем упростить его, вынеся повторяющийся код в отдельную функцию:
```python
def check_parity(n):
     if n % 2 == 0:
        return "Четное"
     else:
        return "Нечетное"

def check_even(n):
    return check_parity(n)

def check_odd(n):
    return check_parity(n)
```
**Пример 2: Дублирование кода в циклах**

Предположим, у нас есть два цикла, которые выполняют одну и ту же задачу - выводят числа от 1 до 10:
```python
for i in range(1, 11):
    print(i)

for j in range(1, 11):
    print(j)
```
Этот код дублируется, и мы можем упростить его, вынеся повторяющийся код в отдельную функцию:
```python
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(10)
print_numbers(10)
```
**Пример 3: Повторяющийся код в условных операторах**

Предположим, у нас есть два условных оператора, которые выполняют одну и ту же задачу - проверяют, является ли число положительным или отрицательным:
```python
if x > 0:
    print("Положительное")
elif x < 0:
    print("Отрицательное")

if y > 0:
    print("Положительное")
elif y < 0:
    print("Отрицательное")
```
Этот код повторяется, и мы можем упростить его, вынеся повторяющийся код в отдельную функцию:
```python
def check_sign(n):
     if n > 0:
        return "Положительное"
     elif n < 0:
        return "Отрицательное"

print(check_sign(x))
print(check_sign(y))
```
**Пример 4: Дублирование кода в классах**

Предположим, у нас есть два класса, которые имеют одинаковые методы:
```python
class Car:
     def __init__(self, color):
        self.color = color
    
     def get_color(self):
        return self.color
    
class Bike:
     def __init__(self, color):
        self.color = color

     def get_color(self):
        return self.color
```
Этот код дублируется, и мы можем упростить его, вынеся повторяющийся код в отдельный класс или интерфейс:
```python
class Vehicle:
     def __init__(self, color):
        self.color = color

     def get_color(self):
        return self.color

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass
```
В каждом из этих примеров мы видим, что повторяющийся код можно упростить, вынеся его в отдельную функцию или метод. Это делает код более читабельным, поддерживаемым и легким для изменения.
