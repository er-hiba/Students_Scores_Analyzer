n = int(input("Enter the number of students: "))

scores = []
Sum = 0

for i in range (n):
    x = float(input(f"Enter the score of the student {i+1}: "))
    scores.append(x)
    Sum += x

scores.sort()
print("The scores in ascending order:", scores)

average = Sum / n
print("The average(mean):", average)

if n % 2 == 0:
    median = (scores[n//2] + scores[n//2 - 1]) / 2
else :
    median = scores [n//2]
print("The median:", median)

sd = []                 # sd stands for squared differences
for x in scores :
    diff = x - average
    sd.append(diff ** 2)

sum_sd = 0
for diff in sd:
    sum_sd += diff

variance = sum_sd / n   # variance (average of squared differences)

std_dev = variance ** 0.5 # square root of variance

print("The standard deviation:", std_dev)

minimum = scores[0]
print("The minimum:", minimum)

maximum = scores[n - 1]
print("The maximum:", maximum)

print("The range:", maximum - minimum)

above_average = []
for i in range (n):
    if scores[i] > average :
        above_average.append(scores[i])

above_average.sort()
print("The scores above average:", above_average)
