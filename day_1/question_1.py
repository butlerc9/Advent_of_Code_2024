input_file = 'question.txt'
# input_file = 'example.txt'

# read in file lines
with open(input_file) as f:
    lines = f.read().split('\n')

left_list = []
right_list = []
for line in lines:
    line = line.split('   ')

    left_digit = int(line[0])
    right_digit = int(line[1])

    left_list.append(left_digit)
    right_list.append(right_digit)

left_list = sorted(left_list)
right_list = sorted(right_list)

sum = sum(abs(l - r) for l, r in zip(left_list,right_list))
print(sum)