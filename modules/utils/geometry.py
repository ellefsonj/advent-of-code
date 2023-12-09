class RectangularCuboid:
    def __init__(self, length, width, height):
        self.dim_l = int(length)
        self.dim_w = int(width)
        self.dim_h = int(height)

    def surface_area(self):
        return 2 * (int(self.dim_l) * int(self.dim_w) + int(self.dim_w) * int(self.dim_h) + int(self.dim_h) * int(self.dim_l))

    def volume(self):
        return self.dim_h * self.dim_w * self.dim_l

    def dimensions_of_smallest_face(self):
        sides = [int(self.dim_l), int(self.dim_w), int(self.dim_h)].sort()
        return sides[:2]

    def dimensions_of_largest_face(self):
        sides = [int(self.dim_l), int(self.dim_w), int(self.dim_h)].sort()
        return sides[1:]

    def area_of_smallest_face(self):
        side = self.dimensions_of_smallest_face()
        return side[0] * side[1]

    def area_of_largest_face(self):
        side = self.dimensions_of_largest_face()
        return side[1] * side[2]

    def perimeter_of_smallest_face(self):
        side = self.dimensions_of_smallest_face()
        return 2 * (sum(side[:2]))

    def perimeter_of_largest_face(self):
        side = self.dimensions_of_smallest_face()
        return 2 * (sum(side[1:]))
