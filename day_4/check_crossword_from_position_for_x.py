def check_crossword_from_position_for_x(crossword, i, j):

    # scan right
    if crossword[i][j] != 'A':
        return 0
    
    up_right = crossword[i - 1][j + 1]
    up_left = crossword[i - 1][j - 1]
    down_right = crossword[i + 1][j + 1]
    down_left = crossword[i + 1][j - 1]
    # print(i,j,up_right,up_left,down_left,down_right)

    if up_left not in ('M','S'):
        return 0
    if up_right not in ('M','S'):
        return 0
    if down_left not in ('M','S'):
        return 0
    if down_right not in ('M','S'):
        return 0
    if up_right == down_left:
        return 0
    if down_right == up_left:
        return 0

    # print(1)
    return 1