class Car1:

    wheels = 4
    num_of_cars = 0

    def __init__(self, model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car1.num_of_cars += 1
    
    def drive(self):
        print(f'you drive the {self.model}')

car1 = Car1('mustang', 2024,'red',False)
car2 = Car1('corveete',2025,'blue',True)
print(car1.__dict__)
print(Car1.num_of_cars)


class Animal:
    def __init__(self,name) -> None:
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def speak(self):
        print('woof')

class Cat(Animal):
    pass

dog = Dog('bobi')
cat = Cat('mitsi')
print(dog.__dict__)



class Prey(Animal):
    def flee(self):
        print('this animal is flee')

class Predator(Animal):
    def hunt(self):
        print('this animal is hunting')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car2(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'abc'

    def go(self):
        print('go')

    def stop(self):
        print('stop')

car5 = Car2()
print(car5.name)

class Shape:
    def __init__(self,color,is_filled) -> None:
        self.color = color
        self.is_filled = is_filled
    

class Circle(Shape):
    def __init__(self, color, is_filled,radius) -> None:
        super().__init__(color, is_filled)
        self.radius = radius


class Library:
    def __init__(self,name) -> None:
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    
    def list_books(self):
        return [f'{book.title}' for book in self.books]

class Book1:
    def __init__(self,title,author) -> None:
        self.title = title
        self.author = author

book1 = Book1('harry potter','g.k.rolling')
book2 = Book1('harry potter2','g.k.rolling')
book3 = Book1('the hobbit','tolkin')

library = Library('new york')
library.add_book(book1)

print(library.books[0].title)
print(library.list_books())

for book in library.list_books():
    print(book)

class Engine:
    def __init__(self,horse_power) -> None:
        self.hors_power = horse_power

class Wheel:
    def __init__(self,size) -> None:
        self.size = size

class Car3:
    def __init__(self,make,model,horse_power,wheel_size) -> None:
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        pass

car1 = Car3('ford', 'mustang', 500, 18)

class Company:
    class Employee:
        def __init__(self,name,positon) -> None:
            self.name = name
            self.positon = positon
        
        def get_detailes(self):
            return f'{self.name} {self.positon}'
    
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.employees = []

    def add_emploee(self,name,position):
        new_employee = self.Employee(name,position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_detailes() for employee in self.employees]

company = Company('krusty_crub')
company.add_emploee('baruch', 'manager')
print(company.list_employees())



class Employee:
    def __init__(self,name,positon) -> None:
        self.name = name
        self.positon = positon
    
    def get_info(self):
        return f'{self.name} {self.positon}'
    
    @staticmethod
    def is_valid(position):
        valid_positions = ['manager','cook']
        return position in valid_positions

print(Employee.is_valid('cook'))

class Student:

    num_students = 0

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        Student.num_students += 1
    

    def get_info(self):
        return self.name
    
    @classmethod
    def get_count(cls):
        return f'total number {cls.num_students}'

print(Student.get_count())

class Book:
    def __init__(self,title,author,num_pages) -> None:
        self.title = title
        self.author = author
        self.num_of_pages = num_pages
    
    def __str__(self) -> str:
        return f'{self.title} by {self.author}'
    
    def __eq__(self,other) -> bool:
        return self.title == other.title

    def __lt__(self,other):
        return self.num_of_pages < other.num_of_pages
    
    def __add__(self,other):
        return self.num_of_pages + other.num_of_pages
    
    def __containes__(self,key_word):
        return key_word in self.title
    
    def __getitem__(self,key):
        if key == "title":
            return self.title

book = Book('the hobbit','j.k.rolling',400)
book2 = Book('the hobbit','j.k.rolling',500)
print(book + book2)

class Rectangle:
    def __init__(self,width,height) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return f'{self.__width} baruch'
    
    @property
    def area(self):
        return self.__width * self.__height

    @width.setter
    def width(self,new_width):
        self.__width = new_width
    
    @width.deleter
    def width(self):
        del self.__width

    
rectangle = Rectangle(3,4)
rectangle.width = 15
print(rectangle.area)

del rectangle.width
# print(rectangle.width)