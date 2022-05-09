# Dictionary

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇

print(key)  # Output Name [Column Header]
print(student_scores[key]) # Output Value [Row]

for key in student_scores:
  student_grades [key] = student_scores[key]  
  if student_grades[key] <= 70:
    student_grades[key] = "Fail"
  elif student_grades[key] <= 80:
    student_grades[key] = "Acceptable"
  elif student_grades[key] <= 90:
    student_grades[key] = "Exceeds Expectations"
  else:
    student_grades[key] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)



