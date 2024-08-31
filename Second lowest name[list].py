numbers_of_input = int(input())

records = []

for x in range(numbers_of_input):
    name = input()
    gpa = float(input())
    records.append([name, gpa])


score = []
for student in records:
    score.append(student[1])

short = sorted(set(score))
second_lowest = short[1]


lower_name = []
for i in records:
    if i[1] == second_lowest:
        lower_name.append(i[0])

sorted_name = sorted(lower_name)
for nam in sorted_name:
    print(nam)
