import re
from remove_invalid_periods import remove_invalid_periods

input_file = 'question.txt'
# input_file = 'example_2.txt'

# read in file lines
with open(input_file) as f:
    file = f.read()

file = remove_invalid_periods(file)

valid_inputs = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)',file)

answer = sum(int(a) * int(b) for a, b in valid_inputs)

print(answer)