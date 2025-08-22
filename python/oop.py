from abc import ABC, abstractmethod #abstract

class Sheap(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def toString(self):#ovverriding
        pass

class Circle(Sheap):
    PI = 3.14

    def __init__(self):
        self.__radius = int(input("Yarıçapı giriniz: "))

    def area(self):
        result = self.PI * self.__radius ** 2#encapsulation
        print("Circle Area:", result)

    def perimeter(self):
        result = 2 * self.PI * self.__radius
        print("Circle Perimeter:", result)

    def toString(self):
        print("Circle toString: Circle with radius", self.__radius)

class Square(Sheap):
    def __init__(self):
        self.__side = int(input("Kenar uzunluğunu giriniz: "))

    def area(self):
        result = self.__side ** 2
        print("Square Area:", result)
    
    def perimeter(self):
        result = 4 * self.__side
        print("Square Perimeter:", result)

    def toString(self):
        print("Square toString: Square with side", self.__side)



c1 = Circle()
c1.area()
c1.perimeter()
c1.toString()

s1 = Square()
s1.area()
s1.perimeter()
s1.toString()
