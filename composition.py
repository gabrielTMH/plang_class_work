class Rectangle:
    def __init__(self, width, height):
       self.width = width
       self.height = height
    def area(self):
       return self.width * self.height
    def perimeter(self):
       return 2 * self.width + 2 * self.height



class Square(Rectangle):
    def __init__(self, width):
        self.width=width
    def rect(self):
        return Rectangle(self.width,self.width)
    def area(self):
        return self.rect().area()
    def perimeter(self):
        return self.rect().perimeter()
    def __setattr__(self, key, value):
        if key != 'width':
            raise TypeError("This class only accepts a width you gave it a "+key)
        else:
            super(Square,self).__setattr__(key,value)


s1 = Square(5)
print(s1.area())
print(s1.perimeter())
s2 = Square(5)
s2.height = 10
print(s2.area())
print(s2.perimeter())