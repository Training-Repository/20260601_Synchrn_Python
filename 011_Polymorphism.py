class Shape:
    def Draw(self):
        pass

    def Fill(self):
        pass

    def BoundaryLength(self):
        pass


class Square:
    def __init__(self, side):
        self.side = side

    def Draw(self):
        print("Drawing...")

    def Fill(self):
        print("Filling...")
    
    def BoundaryLength(self):
        return self.side * 4
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Draw(self):
        print("Drawing...")

    def Fill(self):
        print("Filling...")
    
    def BoundaryLength(self):
        PI = 22/7
        return 2 * PI * self.radius

#---------------------------------------------

def CalculateSideLength(obj:Shape):
    print(f"{type(obj)} -->", obj.BoundaryLength())

sh1: Shape
sh2: Shape

sh1 = Square(10)
sh2 = Circle(10)

CalculateSideLength(sh1)
CalculateSideLength(sh2)
