import pandas as pd
from functools import reduce
from numpy import add
from math import inf
from numpy import mean
import os
import re

NUM_QUIZES = 8
NUM_HOMEWORKS = 4
NUM_MIDTERMS = 2
NUM_PROJECTS = 3
CSV = '2019-05-20T1305_Grades-CMSC421.csv'

def drop(x, num_to_drop):
    if num_to_drop != 0:
        for name in x.nsmallest(num_to_drop).axes:
            x[name] = 0.0
    return x
def exam_grade(x, columns, final_exam_name):
    max_midterm = max(x[columns[0]], x[columns][1])
    scores = list()
    scores.append(x[columns[0]]/200.0 + x[columns[1]]/200.0)
    scores.append(x[final_exam_name]*0.40/200.0 + x[columns[0]]*0.30/100.0 + x[columns[0]]*0.30/100.0)
    scores.append(x[final_exam_name]*0.60/200.0 + max_midterm*0.40/100.0)
    print(x['Student'])
    print(x.name)
    print(scores)
    return max(scores)

def cap_at_B_plus(x):
    if x[final_exam_name] == 0.0 and x['Temp_final'] >= 0.90:
        print(x['Student'])
        print(x['Current Score'])
        print(x['Temp_final'])
        x.loc['Temp_final'] = 0.8999

def calculate_column(name, num_assignments, num_to_drop, contains_string, weight):
    columns = [column for column in old_grades.columns if re.search(contains_string, column)]
    if name != 'final_exam_grade':
        for column in columns:
            old_grades[column] = old_grades[column].map(lambda x: x/old_grades[column][old_grades['Student'] == '    Points Possible'].values[0])
        dropped = old_grades[columns].apply(lambda x: drop(x, num_to_drop), axis=1)
        dropped = dropped.fillna(value=0)
        old_grades[name] = dropped.apply(lambda x: reduce(add, x), axis=1)
        old_grades[name] = old_grades[name].map(lambda x: weight * x / num_assignments)
    else:

        old_grades[name] = old_grades.apply(lambda x: exam_grade(x, columns, final_exam_name), axis=1)
        old_grades[name] = old_grades[name].map(lambda x: weight * x)

old_grades = pd.read_csv(CSV)
old_grades = old_grades.fillna(value=0)
final_exam_name = [column for column in old_grades.columns if re.search(r'Final Exam', column)][0]
calculate_column('final_quiz_grade', NUM_QUIZES, 3, r'Quiz ', 0.05)
calculate_column('final_homework_grade', NUM_HOMEWORKS, 1, r'HW', 0.20)
calculate_column('final_project_grade', NUM_PROJECTS, 0, r'Project[\d]', 0.25)
calculate_column('final_exam_grade', NUM_MIDTERMS, 0, r'Midterm', 0.50)

columns = ['final_quiz_grade', 'final_homework_grade', 'final_project_grade', 'final_exam_grade']
old_grades['Temp_final'] = old_grades[columns].sum(axis=1)
# old_grades.apply(lambda x: cap_at_B_plus(x), axis=1)
print(old_grades[['Current Score', 'Temp_final']])
mean = str(old_grades['Temp_final'].mean())
print('Mean: ' + mean)
median = str(old_grades['Temp_final'].median())
print('Median: ' + median)
std = str(old_grades['Temp_final'].std())
print('Standard deviation: ' + std)