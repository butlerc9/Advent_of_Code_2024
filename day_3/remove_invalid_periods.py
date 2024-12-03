import re

def remove_invalid_periods(input_string):

    cleaned_string = re.sub(
        pattern=r"don't\(\)(.+?)?(do\(\)|\Z)",
        repl='',
        string=input_string,
        flags=re.DOTALL
    )

    return cleaned_string