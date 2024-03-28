class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print
        f"**Car:**\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}"


class Wheels(Car):
    def __init__(self, make, model, year, number, type):
        super().__init__(make, model, year)
        self.number = number
        self.type = type

    def get_info(self):
        info = super().get_info()
        print
        f"{info}\n**Wheels:**\nNumber: {self.number}\nType: {self.type}"


class Engine(Car):
    def __init__(self, make, model, year, type, power):
        super().__init__(make, model, year)
        self.type = type
        self.power = power

    def get_info(self):
        info = super().get_info()
        print
        f"{info}\n**Engine:**\nType: {self.type}\nPower: {self.power}"


class Doors(Car):
    def __init__(self, make, model, year, number, type):
        super().__init__(make, model, year)
        self.number = number
        self.type = type

    def get_info(self):
        info = super().get_info()
        print
        f"{info}\n**Doors:**\nNumber: {self.number}\nType: {self.type}"


car1 = Car("Toyota", "Camry", 2023)
wheels1 = Wheels("Toyota", "Camry", 2023, 4, "Alloy")
engine1 = Engine("Toyota", "Camry", 2023, "Gasoline", 150)
doors1 = Doors("Toyota", "Camry", 2023, 4, "Sedan")

print(car1.get_info())
print(wheels1.get_info())
print(engine1.get_info())
print(doors1.get_info())


# Завдання 3
class Pet:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Ім'я: {self.name}")

    def type(self):
        raise NotImplementedError

    def sound(self):
        raise NotImplementedError


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def type(self):
        print("Пес")

    def sound(self):
        print("Гав!")


class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def type(self):
        print("Кіт")

    def sound(self):
        print("Мяу!")


class Parrot(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def type(self):
        print("Папуга")

    def sound(self):
        print("Крак!")


class Hamster(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def type(self):
        print("Хом'як")

    def sound(self):
        print("Пі-пі!")


dog1 = Dog("Барні", "Лабрадор")
cat1 = Cat("Мурка", "Перська")
parrot1 = Parrot("Кеша", "Жако")
hamster1 = Hamster("Хомка", "Сирійський")

dog1.show()
dog1.type()
dog1.sound()
print("--------------------")

cat1.show()
cat1.type()
cat1.sound()
print("--------------------")

parrot1.show()
parrot1.type()
parrot1.sound()
print("--------------------")

hamster1.show()
hamster1.type()
hamster1.sound()
print()


# Завдання 4
class Employer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print("Це клас Службовець")


class President(Employer):
    def __init__(self, name):
        super().__init__(name)

    def print(self):
        print(f"Це клас Президент, ім'я: {self.name}")


class Manager(Employer):
    def __init__(self, name):
        super().__init__(name)

    def print(self):
        print(f"Це клас Менеджер, ім'я: {self.name}")


class Worker(Employer):
    def __init__(self, name):
        super().__init__(name)

    def print(self):
        print(f"Це клас Працівник, ім'я: {self.name}")


president1 = President("Іван")
manager1 = Manager("Петро")
worker1 = Worker("Марія")

president1.print()
manager1.print()
worker1.print()
print()


# Завдання 5
class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Службовець: {self.name}, вік: {self.age}"

    def __int__(self):
        return self.age


class President(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"Президент: {self.name}, вік: {self.age}"


class Manager(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"Менеджер: {self.name}, вік: {self.age}"


class Worker(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return f"Працівник: {self.name}, вік: {self.age}"


president1 = President("Іван", 55)
manager1 = Manager("Петро", 40)
worker1 = Worker("Марія", 30)

print(president1)
print(int(president1))
print()

print(manager1)
print(int(manager1))
print()

print(worker1)
print(int(worker1))
print()
# Завдання 1
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class CircleInSquare(Circle, Square):
    def __init__(self, radius):
        super().__init__(radius)
        self.side = 2 * radius

    def square_area(self):
        return self.side ** 2

    def __str__(self):
        return f"Circle in square:\nPerimeter of a circle: {Circle.perimeter(self)}\nPerimeter of a Square: {Square.perimeter(self)}\nRadius: {self.radius}\nSide of square: {self.side}\nCircle area: {Circle.area(self)}\nSquare area: {self.square_area()}"


obj = CircleInSquare(5)
print(obj)
