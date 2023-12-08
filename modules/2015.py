import csv


def day_one_runner():
    floor = 0
    index = 1
    basement_found = False
    sequence = ''
    with open('../resources/2015/puzzle_one_part_1.csv', newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for line in reader:
            sequence = line[0]
    for c in sequence:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor < 0 and not basement_found:
            basement_found = True
        elif not basement_found:
            index += 1
    print('Ending Floor:' + str(floor))
    print('Position of first direction entering basement: ' + str(index))


class Present:
    def __init__(self, length, width, height):
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)

    def surface_area(self):
        return 2 * int(self.length) * int(self.width) + 2 * int(self.width) * int(self.height) + 2 * int(
            self.height) * int(self.length)

    def volume(self):
        return self.height * self.width * self.length

    def smallest_side_dimensions(self):
        sides = [int(self.length), int(self.width), int(self.height)]
        sides.sort()
        return sides[:2]

    def area_of_smallest_side(self):
        side = self.smallest_side_dimensions()
        return side[0] * side[1]

    def perimeter_of_smallest_side(self):
        side = self.smallest_side_dimensions()
        return 2 * side[0] + 2 * side[1]

    def ribbon_length_needed(self):
        return self.volume() + self.perimeter_of_smallest_side()

    def wrapping_paper_square_units(self):
        return self.surface_area() + self.area_of_smallest_side()


def day_two_runner():
    presents = []
    total_wrapping_paper_needed = 0
    total_ribbon_needed = 0
    with open('../resources/2015/puzzle_two.csv', newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for line in reader:
            values = line[0].split('x')
            present = Present(int(values[0]), int(values[1]), int(values[2]))
            total_wrapping_paper_needed += present.wrapping_paper_square_units()
            total_ribbon_needed += present.ribbon_length_needed()
            presents.append(present)
    print('Total Wrapping Paper Needed (square feet): ' + str(total_wrapping_paper_needed))
    print('Total Ribbon Needed (feet): ' + str(total_ribbon_needed))


def main():
    # day_one_runner()
    # day_two_runner()


if __name__ == "__main__":
    main()
