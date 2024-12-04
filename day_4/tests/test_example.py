from check_crossword_from_position import check_crossword_from_position


def test_example_input():
    
    number_per_scan = check_crossword_from_position(crossword=['XMAS'], i=0, j=0, target_word='XMAS')

    assert number_per_scan == 1
