from check_crossword_from_position import check_crossword_from_position

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
for i in range(m):
    for j in range(n):
        target_word_count += check_crossword_from_position(crossword=crossword, i=i, j=j, target_word=target_word)

print(target_word_count)