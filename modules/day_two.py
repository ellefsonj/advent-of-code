import modules.filereader as fr


class Result:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Game:
    def __init__(self, game_id, result_set):
        self.game_id = game_id
        self.result_set = result_set

    def max_red(self):
        max_count = 0
        for result in self.result_set:
            if result.red > max_count:
                max_count = result.red
        return max_count

    def max_green(self):
        max_count = 0
        for result in self.result_set:
            if result.green > max_count:
                max_count = result.green
        return max_count

    def max_blue(self):
        max_count = 0
        for result in self.result_set:
            if result.blue > max_count:
                max_count = result.blue
        return max_count

    def is_result_set_possible(self, red, green, blue):
        return self.max_red() <= red and self.max_green() <= green and self.max_blue() <= blue

    def get_power_of_minimum_cube_values(self):
        return self.max_red() * self.max_green() * self.max_blue()


def execute():
    games = fr.read_file_for_game_data('resources/puzzle_two_input.csv')
    sum_of_game_ids_with_possible_result = 0
    sum_of_powers = 0
    for game in games:
        if game.is_result_set_possible(12, 13, 14):
            sum_of_game_ids_with_possible_result += game.game_id
        sum_of_powers += game.get_power_of_minimum_cube_values()

    print('Part 1: Sum of Game Ids With Possible Results: ' + str(sum_of_game_ids_with_possible_result))
    print('Part 2: Sum of Powers of Minimum Cubes: ' + str(sum_of_powers))
