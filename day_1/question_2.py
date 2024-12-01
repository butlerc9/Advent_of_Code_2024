input_file = 'question.txt'
# input_file = 'example.txt'

# read in file lines
with open(input_file) as f:
    lines = f.read().split('\n')

left_list = []
right_dict = {}
for line in lines:
    line = line.split('   ')

    left_digit = int(line[0])
    right_digit = int(line[1])

    left_list.append(left_digit)

    # create a dictionary with digit frequencies
    if right_digit not in right_dict:
        right_dict[right_digit] = 1
    else:
        right_dict[right_digit] += 1

similarity_score = 0
for l in left_list:
    if l in right_dict:
        similarity_score += l * right_dict[l]