from math import pow, sqrt
import matplotlib.pyplot as plt


class AbstractFigure:
    __count = 0
    plot = plt

    def __init__(self, plotter):
        AbstractFigure.__count += 1
        self.id = AbstractFigure.__count
        self.plot = plotter

    def draw_line(self, x_values, y_values, color):
        self.plot.plot(x_values, y_values, linewidth=0.25, color=color)

    @classmethod
    def how_many_figures(cls):
        return cls.__count

    @classmethod
    def plot_all(cls):
        cls.plot.show()


class Triangle(AbstractFigure):
    def __init__(self, a=(0, 0), b=(0, 1), c=(1, 0)):
        super(Triangle, self).__init__(plt)
        self.point_1 = a
        self.point_2 = b
        self.point_3 = c

    def __repr__(self):
        return f"Trikampis id: {self.id}, A: {self.point_1}, B: {self.point_2}, C: {self.point_3}"

    def perimeter(self):
        # 1ma nuo self.point_1 iki self.point_2
        first_line = sqrt(pow(self.point_2[0] - self.point_1[0], 2) + pow(self.point_2[1] - self.point_1[1], 2))
        # 2a nuo self.point_2 iki self.point_3
        second_line = sqrt(pow(self.point_3[0] - self.point_2[0], 2) + pow(self.point_3[1] - self.point_2[1], 2))
        # 3ia nuo self.point_3 iki self.point_1
        third_line = sqrt(pow(self.point_1[0] - self.point_3[0], 2) + pow(self.point_1[1] - self.point_3[1], 2))
        perimeter = first_line + second_line + third_line
        return perimeter

    def plot_me(self):
        l1_x_values = [self.point_1[0], self.point_2[0]]
        l1_y_values = [self.point_1[1], self.point_2[1]]
        self.plot.plot(l1_x_values, l1_y_values, linewidth=0.25, color='red')
        l2_x_values = [self.point_2[0], self.point_3[0]]
        l2_y_values = [self.point_2[1], self.point_3[1]]
        self.plot.plot(l2_x_values, l2_y_values, linewidth=0.25, color='red')
        l3_x_values = [self.point_3[0], self.point_1[0]]
        l3_y_values = [self.point_3[1], self.point_1[1]]
        self.plot.plot(l3_x_values, l3_y_values, linewidth=0.25, color='red')




class Rectangle(AbstractFigure):
    def __init__(self, a=(0, 0), b=(0, 1), c=(1, 0), d=(1, 1), colour='red'):
        super(Rectangle, self).__init__(plt)
        self.colour = colour
        self.point_1 = a
        self.point_2 = b
        self.point_3 = c
        self.point_4 = d
        self.l1 = sqrt(pow(self.point_1[0] - self.point_2[0], 2) + pow(self.point_2[1] - self.point_1[1], 2))
        self.l2 = sqrt(pow(self.point_3[0] - self.point_2[0], 2) + pow(self.point_3[1] - self.point_2[1], 2))
        self.l3 = sqrt(pow(self.point_4[0] - self.point_3[0], 2) + pow(self.point_4[1] - self.point_3[1], 2))
        self.l4 = sqrt(pow(self.point_1[0] - self.point_4[0], 2) + pow(self.point_1[1] - self.point_4[1], 2))
        self.check_valid(self.l1, self.l2, self.l3, self.l4)

    def __repr__(self):
        return f"Kvadratas A: {self.point_1}, B: {self.point_2}, C: {self.point_3}, D: {self.point_4}"

    def perimeter(self):
        return self.l1 + self.l2 + self.l3 + self.l4

    @classmethod
    def check_valid(cls, l1, l2, l3, l4):
        if l1 != l3:
            raise ValueError(f'l1:{l1} nelygu l3:{l3}')

        if l2 != l4:
            raise ValueError(f'l2:{l2} nelygu l4:{l4}')

    def plot_me(self):
        l1_x_values = [self.point_1[0], self.point_2[0]]
        l1_y_values = [self.point_1[1], self.point_2[1]]
        self.draw_line(l1_x_values, l1_y_values, self.colour)
        l2_x_values = [self.point_2[0], self.point_3[0]]
        l2_y_values = [self.point_2[1], self.point_3[1]]
        self.draw_line(l2_x_values, l2_y_values, self.colour)
        l3_x_values = [self.point_3[0], self.point_4[0]]
        l3_y_values = [self.point_3[1], self.point_4[1]]
        self.draw_line(l3_x_values, l3_y_values, self.colour)
        l4_x_values = [self.point_4[0], self.point_1[0]]
        l4_y_values = [self.point_4[1], self.point_1[1]]
        self.draw_line(l4_x_values, l4_y_values, self.colour)


if __name__ == "__main__":
    triangle_data = [
        ((1, 2), (1, 6), (2, 4)),
        ((2, 3), (2, 7), (3, 5)),
        ((3, 4), (3, 8), (8, 6)),
    ]
    square_data = [
        ((1, 2), (1, 6), (6, 6), (6, 2), 'blue'),
        ((1, 2), (1, 3), (3, 3), (3, 2), 'green'),
        ((1, 1), (1, 8), (4, 8), (4, 1), 'red'),
    ]
    new_triangles = []
    new_square = []

    for t_data in triangle_data:
        a = t_data[0]
        b = t_data[1]
        c = t_data[2]
        naujas_trikampis = Triangle(a, b, c)
        new_triangles.append(naujas_trikampis)
        naujas_trikampis.plot_me()
        print(naujas_trikampis.perimeter())

    for t_data in square_data:
        a = t_data[0]
        b = t_data[1]
        c = t_data[2]
        d = t_data[3]
        colour = t_data[4]
        try:
            naujas_kvadratas = Rectangle(a, b, c, d, colour)
            new_square.append(naujas_kvadratas)
            naujas_kvadratas.plot_me()
            print(naujas_kvadratas.perimeter())

        except ValueError as r:
            print(r, t_data)
            continue

    Rectangle.plot_all()

    number_of_objects = new_triangles[0].how_many_figures()
    print(f'number of triangles: {number_of_objects}')

