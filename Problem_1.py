'''
Given the names and grades for each student in a Physics class of  students
store them in a nested list and print the name(s) of any student(s) having
the second lowest grade.'

Note: If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line.

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
'''

N = int(input())

students = []
for _ in range(2 * N):
    students.append(input().split())

scores = {}
for element in range(0, len(students), 2):
    scores[students[element][0]] = float(students[element + 1][0])

lowest_second = sorted(set(scores.values()))[1]

result = []
for i in scores.keys():
    if scores[i] == lowest_second:
        result.append(i)

for k in sorted(result):
    print(k)
