n = int(input("Enter the number of students: "))

students_scores = []
Sum = 0
for i in range (n):
    x = float(input(f"Enter the score of the student {i+1}: "))
    students_scores.append(x)
    Sum += x

average = Sum / n
print("The average is: ", average)

List = []
for i in range (n):
    if students_scores[i] > average :
        List.append(students_scores[i])

List.sort()
print("Scores above average are:", List)
