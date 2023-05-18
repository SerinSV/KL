class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        print(area)

    def perimeter(self):
        perimeter = 4 * self.side
        print(perimeter)


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print(area)

    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print(perimeter)


class Triangle:
    def __init__(self, a):
        self.a = a

    def area(self):
        area = 0.433 * (self.a * self.a)
        print(area)

    def perimeter(self):
        perimeter = 3 * self.a
        print(perimeter)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * (self.radius * self.radius)
        print(area)

    def perimeter(self):
        perimeter = 6.28 * self.radius
        print(float(perimeter))


sq = Square(4)
sq.area()
sq.perimeter()
rec = Rectangle(4, 6)
rec.area()
rec.perimeter()
tri = Triangle(6)
tri.area()
tri.perimeter()
cir = Circle(5)
cir.area()
cir.perimeter()
