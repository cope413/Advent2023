from icecream import ic
import re

raw_input = "Day2_part1.txt"
games = {}
with open(raw_input, 'r') as file:
    data = file.readlines()
    for line in data:
        game_match = re.search(r'Game (\d+)', line)
        digits_before_green = re.findall(r'(\d+)\s+green', line)
        digits_before_blue = re.findall(r'(\d+)\s+blue', line)
        digits_before_red = re.findall(r'(\d+)\s+red', line)
        game_number = int(game_match.group(1))
        largest_green = max(map(int, digits_before_green))
        largest_blue = max(map(int, digits_before_blue))
        largest_red = max(map(int, digits_before_red))
        games.update({game_number: (largest_green, largest_blue, largest_red)})

total = 0
for x in range(1,len(games)):
    if games[x][0] <= 13 and games[x][1] <= 14 and games[x][2] <= 12:
        total += x

ic(total)

