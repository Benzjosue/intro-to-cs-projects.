'''
Program name: Grades and Attendance
Author name: Benz Josue
Description: This program stores students exam grades as a list 
             and students attendance as a set.
'''

exam_grades = {83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80}
day1_attn = {'Mary', 'Jake', 'Sam', 'Alex', 'Percy', 'Jessica,','Trent', 'Mahmoud'}
day2_attn = {'Jake', 'Sam', 'Alex', 'Percy', 'Mahmoud', 'Trent', 'Caleb', 'Zayne'}

# Grade
# a. How many Students took the exam?
num_exam = len(exam_grades)
print(f'{num_exam} Students took the exam. ')

# b. What was the highest grade?
highest = max(exam_grades)
print(f'The highest exam grade was {highest}')
      
# c. What was the lowest exam grade?
lowest = min(exam_grades)
print(f'The lowest exam grade was {lowest}')

# d.  What was the class average for the exam?
average = sum(exam_grades) / len(exam_grades)
print(f'The average grade for the exam was a {average:.1f}')



# Attendance
# a. How many students attended the class?
print(len(day1_attn.union(day2_attn)), 'students attended the class.')

# b. Who attended both days of class?
print(day1_attn.intersection(day2_attn), 'attended both class days.')

# c. Who attended only one day of class?
#print(day1_attn.union(day2_attn) - day1_attn.intersection(day2_attn), 'attended one class.')
print(day1_attn.symmetric_difference(day2_attn), 'attended one class day.')
