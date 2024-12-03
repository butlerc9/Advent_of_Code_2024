import re

input_file = 'question.txt'
# input_file = 'example.txt'

# read in file lines
with open(input_file) as f:
    file = f.read()

valid_inputs = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)',file)

answer = sum(int(a) * int(b) for a, b in valid_inputs)

print(answer)