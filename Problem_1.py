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
number_of_student = int(input())

students_data = [[input(), float(input())] for _ in range(number_of_student)]

lowest_second = sorted(list(set([grade for name, grade in students_data])))[1]

result = [name for name, grade in students_data if grade == lowest_second]

print('\n'.join(sorted(result)))
