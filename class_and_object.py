from abc import ABC, abstractmethod
import os


class Rectangle:

    # Class Attribute
    color = '#0f0'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_area(self):
        return self.x * self.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        rect = Rectangle(x, y)
        return rect


d = Rectangle(10, 20)
print('2D x: ', d.get_x())
print('2D y: ', d.get_y())
print('2D area: ', d.get_area())

# inheritance single


class Cube(Rectangle):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def get_z(self):
        return self.z

    def get_volume(self):
        return self.get_area() * self.z


d3 = Cube(10, 20, 30)
print('3D x: ', d3.get_x())
print('3D y: ', d3.get_y())
print('3D z: ', d3.get_z())
print('3D area: ', d3.get_area())
print('3D volume: ', d3.get_volume())


# inheritance multi level
'''
class A:
    def feature1(self):
        return 'feature 1'


class B(A):
    def feature2(self):
        return 'feature 2'


class C(B):
    def feature3(self):
        return 'feature 3'


# inheritance multiple


class A:
    def feature1(self):
        return 'feature 1'


class B:
    def feature2(self):
        return 'feature 2'


class C(A, B):
    def feature3(self):
        return 'feature 3'
'''

'''
# nesting of classes
class Student:
    # Class Attribute
    total_student = 100
    total_mark = 100

    def __init__(self, mark):
        self.computer = self.Computer()
        self.mark = mark

    def get_rank(self):
        return (self.mark / self.total_mark) * self.total_student

    class Computer:
        def get_config(self):
            return 'i5 Lenovo 15 inch UHD'


s = Student(20)
print('Student rank:', s.get_rank())
print('Student computer:', s.computer.get_config())
print('Student 2 computer:', Student(20).Computer().get_config())
'''

'''
class Server:
    __domain = 'https://example.com'

    @classmethod
    def get_domain(cls):
        return cls.__domain

    @staticmethod
    def get_JAVA_PATH():
        return os.environ.get('JAVA_HOME')


print('Server OS: ', Server.get_domain())
print('JAVA located at: ', Server.get_JAVA_PATH())
'''

# polymorphism
# Dock typing
'''
print('############### polymorphism ###################')

print('############### Dock typing ###################')


class VsCode:
    def execute(self):
        print('loading...')
        print('parsing...')
        print('compiling...')
        print('output')


class Anaconda:
    def execute(self):
        print('loading...')
        print('parsing...')
        print('splitting into chunks...')
        print('creating threads...')
        print('compiling...')
        print('output')


class Computer:
    def code(self, ide):
        ide.execute()


c1 = Computer()
c2 = Computer()

c1.code(VsCode())
c1.code(Anaconda())

print('############### Operator overloading ###################')

a = 10
b = 20
print(a + b)
print(int.__add__(a, b))

rect1 = Rectangle(10, 20)
rect2 = Rectangle(20, 30)
rect3 = rect1 + rect2
print('New rect x: ', rect3.get_x())
print('New rect y: ', rect3.get_y())

print('############### Method overloading ###################')
print('############### Not present in python ###################')
'''

# Abstract class
'''
print("Abstract class")
print("cannot create instance")
print("python does not support")


class Vehicle:
    @abstractmethod
    def get_wheels(self):
        pass

    def get_model(self):
        pass


print(Vehicle())


class Car(Vehicle):
    def get_wheels(self):
        return 'four'

    def get_model(self):
        return 'NA'


car = Car()
print('Car wheels: ', car.get_wheels())
print('Car wheels: ', car.get_model())
'''
