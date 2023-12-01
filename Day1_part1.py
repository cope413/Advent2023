numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
raw_input = r"Day1_part1.txt"

two_digit = []

with open(raw_input, 'r') as file:
    data = file.readlines()
    for line in data:
        sequence = []
        for n in line:
            if n in numbers:
                sequence.append(n)
        two_digit.append(int(sequence[0]))
        two_digit.append(int(sequence[-1]))


def combine_digits(num_list):
    combined_nums = []

    for i in range(0, len(two_digit), 2):
        first_digit = two_digit[i]

        if i < len(two_digit) - 1:
            second_digit = two_digit[i + 1]
        else:
            second_digit = 0

        combined_num = int(str(first_digit) + str(second_digit))
        combined_nums.append(combined_num)

    return combined_nums


new_list = combine_digits(two_digit)
total = 0
for n in new_list:
    total += n
print(total)

