import csv
import re
import modules.day_two as day_two


def readFileToArray(filePath):
    lines = []
    with open(filePath, newline='') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in reader:
            lines.append(row)
        return lines


def read_file_for_game_data(filePath):
    games = []
    with open(filePath, newline='') as file:
        reader = csv.reader(file, delimiter=':')
        for row in reader:
            game_id = int(determine_game_id(row[0]))
            result_set = determine_result_set(row[1])
            games.append(day_two.Game(game_id, result_set))
    return games


def determine_game_id(value):
    match = re.search(r'\d+', value)
    if match:
        return match.group()
    else:
        return 0


def build_result(pull_data):
    split_pull_data = pull_data.split(',')
    red = green = blue = 0
    for data in split_pull_data:
        count_match = re.search(r'\d+', data)
        color_match = re.search(r'red|green|blue', data)
        if color_match and 'red' == color_match.group():
            red = int(count_match.group())
        elif color_match and 'green' == color_match.group():
            green = int(count_match.group())
        elif color_match and 'blue' == color_match.group():
            blue = int(count_match.group())
        else:
            print('Unable to properly process: ' + str(data))

    return day_two.Result(red, green, blue)


def determine_result_set(game_data):
    result_set = []
    split_game_data = game_data.split(';')
    for data in split_game_data:
        result_set.append(build_result(data))
    return result_set
