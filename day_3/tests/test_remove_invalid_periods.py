from remove_invalid_periods import remove_invalid_periods

def test_normal_example():
    
    string = 'a'

    assert remove_invalid_periods(string) == 'a'

def test_example_with_only_dont():
    
    string = "adon't()a"

    assert remove_invalid_periods(string) == 'a'

def test_example_with_dont_and_do():
    
    string = "adon't()ado()a"

    assert remove_invalid_periods(string) == 'aa'

def test_example_with_dont_at_the_end():
    
    string = "adon't()a"

    assert remove_invalid_periods(string) == 'a'

def test_example_with_multiple_donts_at_the_end():
    
    string = "adon't()adon't()a"

    assert remove_invalid_periods(string) == 'a'

def test_example_with_multiple_dos_and_donts_at_the_end():
    
    string = "adon't()dasfdo()adon't()a"

    assert remove_invalid_periods(string) == 'aa'

def test_example_with_multiple_dos_and_donts_at_the_end():
    
    string = "adon't()dasfdo()adon't()do()don't()aasdfdo()"

    assert remove_invalid_periods(string) == 'aa'
