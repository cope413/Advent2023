from icecream import ic

raw_input = r"Day1_part1.txt"

number_dict = {"twone": 21,
               "eightwo": 82,
               "oneight": 18,
               "fiveight": 58,
               "nineight": 98,
               "threeight": 38,
               "sevenine": 79,
               "one": 1,
               "two": 2,
               "three": 3,
               "four": 4,
               "five": 5,
               "six": 6,
               "seven": 7,
               "eight": 8,
               "nine": 9,
               }
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
two_digit = []
input_list = []

with open(raw_input, 'r') as file:
    data = file.readlines()
    for line in data:
        input_list.append(line.rstrip())

for i in range(len(input_list)):
    for key, value in number_dict.items():
        input_list[i] = input_list[i].replace(key, str(value))


numbers_only = [''.join(n for n in calib_num if n in numbers) for calib_num in input_list]

new_list = [int(''.join(string[0] + string[-1])) for string in numbers_only]


total = 0
for num in new_list:
    total += num
ic(sum(new_list))
