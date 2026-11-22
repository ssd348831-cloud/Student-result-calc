from calc import calculate_total, calculate_avg
from grades import get_grade
score1 = int(input("Put score1 here"))
score2 = int(input("Put score2 here"))
score3 = int(input("Put score3 here"))

total = calculate_total(score1, score2, score3) 
avg = calculate_avg(total)
grade = get_grade(avg)

print(f"Total score: {total}")
print(f"avg score: {avg}")
print(f"grade: {grade}")

