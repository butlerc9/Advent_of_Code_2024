from report_safety_analyser_with_dampner import report_safety_analyser_with_dampner

# input_file = 'question.txt'
input_file = 'example.txt'

# read in file lines
with open(input_file) as f:
    lines = f.read().split('\n')

number_of_safe_reports = 0
for report in lines:
    report = report.split(' ')
    report = [int(digit) for digit in report]
    number_of_safe_reports += report_safety_analyser_with_dampner(report)

print(number_of_safe_reports)