from check_crossword_from_position_for_x import check_crossword_from_position_for_x

input_file = 'question.txt'
# input_file = 'example.txt'
# input_file = 'example.txt'

# read in file lines
with open(input_file) as f:
    crossword = f.read().split('\n')

m = len(crossword)
n = len(crossword[0])
target_word = 'XMAS'

target_word_count = 0
for i in range(1,m-1):
    for j in range(1,n-1):
        target_word_count += check_crossword_from_position_for_x(crossword=crossword, i=i, j=j)

print(target_word_count)