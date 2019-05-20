# grade_script_CMSC_421
Script written for calculating the final grades in CMSC 421

Grading Procedure:

1. For each student, count all but the three lowest quiz scores (out of 11) and the one lowest hwk score (out of 5)

2. For each student, calculate their numerical total score in three ways:
a. ignoring final_exam scores, and using 25% for each midterm
b. using the final (even if they did not take it) and both midterms as: 20%, 15%, 15%
c. using the final as 30% (even if they did not take it) and the higher midterm as 20% (do not count the lower midterm)

3. Pick the best of the three grades (a-b-c)

4. Determine letter cutoffs

5. For any students who did not take the final but whose total score is *above* B+, reduce it to B+.

Homeworks: 15% Drop 1
Quizes: 5% drop 3
Projects: 25%
Exams: 50%

