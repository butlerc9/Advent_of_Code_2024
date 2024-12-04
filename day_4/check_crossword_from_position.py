def check_crossword_from_position(crossword, i, j, target_word):

    m = len(crossword)
    n = len(crossword[0])

    # check horizontal
    enough_space_to_scan_right = j + len(target_word) <= n
    enough_space_to_scan_left = j - len(target_word) + 1 >= 0
    enough_space_to_scan_up = i - len(target_word) + 1 >= 0
    enough_space_to_scan_down = i + len(target_word) <= m 

    print(i, j, enough_space_to_scan_right,enough_space_to_scan_left, enough_space_to_scan_up, enough_space_to_scan_down)

    number_of_target_words_found_in_scan = 0

    # scan right
    if enough_space_to_scan_right:
        right_word = ''.join(crossword[i][j + k] for k in range(len(target_word)))
        if right_word == target_word:
            number_of_target_words_found_in_scan += 1
    # scan left
    if enough_space_to_scan_left:
        left_word = ''.join(crossword[i][j - k] for k in range(len(target_word)))
        print(left_word)
        if left_word == target_word:
            number_of_target_words_found_in_scan += 1
    # scan down
    if enough_space_to_scan_down:
        down_word = ''.join(crossword[i + k][j] for k in range(len(target_word)))
        if down_word == target_word:
            number_of_target_words_found_in_scan += 1
    # scan up
    if enough_space_to_scan_up:
        up_word = ''.join(crossword[i - k][j] for k in range(len(target_word)))
        if up_word == target_word:
            number_of_target_words_found_in_scan += 1

    # scan up right
    if enough_space_to_scan_up and enough_space_to_scan_right:
        right_word = ''.join(crossword[i - k][j + k] for k in range(len(target_word)))
        if right_word == target_word:
            number_of_target_words_found_in_scan += 1
    # scan up left
    if enough_space_to_scan_up and enough_space_to_scan_left:
        left_word = ''.join(crossword[i - k][j - k] for k in range(len(target_word)))
        if left_word == target_word:
            number_of_target_words_found_in_scan += 1
    # scan down right
    if enough_space_to_scan_down and enough_space_to_scan_right:
        down_word = ''.join(crossword[i + k][j + k] for k in range(len(target_word)))
        if down_word == target_word:
            number_of_target_words_found_in_scan += 1
    # scan down left
    if enough_space_to_scan_down and enough_space_to_scan_left:
        up_word = ''.join(crossword[i + k][j - k] for k in range(len(target_word)))
        if up_word == target_word:
            number_of_target_words_found_in_scan += 1

    return number_of_target_words_found_in_scan