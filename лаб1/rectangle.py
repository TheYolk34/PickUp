from geometric_figure import GeometricFigure
from color_figure import ColorFigure

class Rectangle(GeometricFigure):
    figure_type = "Прямоугольник"

    def __init__(self, width, height, color):
        super().__init__()
        self.width = width
        self.height = height
        self.color = ColorFigure(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета, ширина {}, высота {}, площадь {}".format(
            self.figure_type, self.color.color, self.width, self.height, self.area()
        )