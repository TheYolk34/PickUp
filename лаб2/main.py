from rectangle import Rectangle
from square import Square
from circle import Circle


def main():
    # Пример использования
    rectangle = Rectangle(6, 6, "синего")
    circle = Circle(6, "зеленого")
    square = Square(6, "красного")

    print(rectangle)
    print(circle)
    print(square)

if __name__ == "__main__":
    main()
    input()