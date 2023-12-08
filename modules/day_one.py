import modules.filereader as fr
import re


def find_first_numeric_value(val, reverse):
    if reverse:
        match = re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez', val[::-1])
    else:
        match = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine|zero', val)

    if match:
        return convert_alphabetic_digit_to_numeric(match.group())
    else:
        return 0


def convert_alphabetic_digit_to_numeric(val):
    numbers = [
        ['zero', 0],
        ['one', 1],
        ['two', 2],
        ['three', 3],
        ['four', 4],
        ['five', 5],
        ['six', 6],
        ['seven', 7],
        ['eight', 8],
        ['nine', 9]
    ]

    match = re.search(r'\d', val)
    if match:
        return match.group()
    else:
        for number in numbers:
            if val == number[0] or val == number[0][::-1]:
                return number[1]
        return ''


def determine_calibration_value(val):
    return str(find_first_numeric_value(val, False)) + str(find_first_numeric_value(val, True))


def execute():
    lines = fr.readFileToArray('resources/puzzle_one_input.csv')
    total_sum_of_calibration_value = 0
    iteration = 0;
    for line in lines:
        calibration_value = determine_calibration_value(str(line[0]))
        iteration += 1
        print(str(iteration) + ':' + str(line[0]) + " : " + calibration_value)
        total_sum_of_calibration_value += int(calibration_value)
    #print('Determined Sum of Calibration Values: ' + str(total_sum_of_calibration_value) + '.')
