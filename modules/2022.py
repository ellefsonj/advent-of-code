import csv


class Elf:

    def __init__(self, elf_id, calories):
        self.elf_id = elf_id
        self.calories = calories

    def total_calories(self):
        total_calories = 0
        for calorie_amount in self.calories:
            total_calories += calorie_amount
        return total_calories


def day_one_runner():
    elves = []

    calories = [[]]
    with open('../resources/2022/2022_day_1_part_1.csv', newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        calorie_index = 0
        for row in reader:
            if len(row) > 0:
                calories[calorie_index].append(int(row[0]))
            else:
                calories.append([])
                calorie_index += 1
    elf_id = 1
    for calorie_set in calories:
        elves.append(Elf(elf_id, calorie_set))
        elf_id += 1
    max_calories = 0
    second_max_calories = 0
    third_max_calories = 0
    for elf in elves:
        if elf.total_calories() > max_calories:
            third_max_calories = second_max_calories
            second_max_calories = max_calories
            max_calories = elf.total_calories()
        elif elf.total_calories() > second_max_calories:
            third_max_calories = second_max_calories
            second_max_calories = elf.total_calories()
        elif elf.total_calories() > third_max_calories:
            third_max_calories = elf.total_calories()

    print('One: ' + str(max_calories))
    print('Second: ' + str(second_max_calories))
    print('Three: ' + str(third_max_calories))
    print('Sum of Top 3: ' + str(max_calories + second_max_calories + third_max_calories))

def day_two_runner():
    print('Hello')


def main():
    day_one_runner()


if __name__ == "__main__":
    main()
