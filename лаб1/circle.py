from geometric_figure import GeometricFigure
from color_figure import ColorFigure
import math

class Circle(GeometricFigure):
    figure_type = "Круг"

    def __init__(self, radius, color):
        super().__init__()
        self.radius = radius
        self.color = ColorFigure(color)

    def area(self):
        return math.pi * self.radius**2

    def __repr__(self):
        return "{} {} цвета, радиус {}, площадь {:.2f}".format(
            self.figure_type, self.color.color, self.radius, self.area()
        )
