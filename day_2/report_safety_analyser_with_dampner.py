from report_safety_analyser import report_safety_analyser

def report_safety_analyser_with_dampner(report):

    print('report: ',report)
    # handle case with 2 entries
    if len(report) <= 2:
        return True

    for level_index in range(len(report)):
        
        subreport = report[:level_index] + report[level_index+1 :]
        
        if report_safety_analyser(subreport):
            return True
    
    return False