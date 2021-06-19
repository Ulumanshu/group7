from math import pow, sqrt


class Triangle:
    def __init__(self, a=(0, 0), b=(0, 1), c=(1, 0)):
        self.point_1 = a
        self.point_2 = b
        self.point_3 = c

    def __repr__(self):
        return f"Trikampis A: {self.point_1}, B: {self.point_2}, C: {self.point_3}"

    def perimeter(self):
        # 1ma nuo self.point_1 iki self.point_2
        first_line = sqrt(pow(self.point_2[0] - self.point_1[0], 2) + pow(self.point_2[1] - self.point_1[1], 2))
        # 2a nuo self.point_2 iki self.point_3
        second_line = sqrt(pow(self.point_3[0] - self.point_2[0], 2) + pow(self.point_3[1] - self.point_2[1], 2))
        # 3ia nuo self.point_3 iki self.point_1
        third_line = sqrt(pow(self.point_1[0] - self.point_3[0], 2) + pow(self.point_1[1] - self.point_3[1], 2))
        perimeter = first_line + second_line + third_line
        return perimeter


if __name__ == "__main__":
    triangle_data = [
        ((1, 2), (1, 6), (2, 4)),
    ]
    new_triangles = []
    for t_data in triangle_data:
        a = t_data[0]
        b = t_data[1]
        c = t_data[2]
        naujas_trikampis = Triangle(a, b, c)
        new_triangles.append(naujas_trikampis)

    print(new_triangles)
    for triangle in new_triangles:
        print(triangle.perimeter())

 # trikampis1 = Triangle()
# print(trikampis1.point_1, trikampis1.point_2, trikampis1.point_3)