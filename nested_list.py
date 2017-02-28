# Store each student's name and grade in a nested list, print the names that have the second lowest grade.
# problem from Hackerrank.
# n=number of students.


n = 5
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


temp = []
for i in xrange(len(students)):
    temp.append(students[i][1])

minGrade = min(temp)
while min(temp) == minGrade:
    temp.remove(minGrade)

    
name = []
for j in xrange(len(students)):
    if students[j][1] == min(temp):
        name.append(students[j][0])
print '\n'.join(sorted(name))
