def report_safety_analyser(report):

    # handle case with only one entry
    if len(report) == 1:
        return True

    if report[0] < report[1]:
        ascending = True
    else:
        ascending = False


    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) > 3:
            return False
        elif ascending and report[i] >= report[i+1]:
            return False
        elif ascending is False and report[i] <= report[i+1]:
            return False
    
    return True