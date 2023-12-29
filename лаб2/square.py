from rectangle import Rectangle

class Square(Rectangle):
    figure_type = "Квадрат"

    def __init__(self, side_length, color):
        super().__init__(side_length, side_length, color)