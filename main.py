import math

class Polygon:
    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

class Square(Polygon):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2

def main():
    print("Choose a polygon to calculate area:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")

    choice = input("Enter your number of choice: ")
    
    if choice == '1':
        side = float(input("Enter the side length of the square: "))
        square = Square(side)
        print(f"The area of the square is: {square.area()}")

    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rectangle = Rectangle(length, width)
        print(f"The area of the rectangle is: {rectangle.area()}")

    elif choice == '3':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        triangle = Triangle(base, height)
        print(f"The area of the triangle is: {triangle.area()}")

    elif choice == '4':
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)
        print(f"The area of the circle is: {circle.area()}")

    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()