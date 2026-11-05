
data = {}
data['name'] = 'John'
data['age'] = 35
data['gpa'] = 3.5

print(data['gpa'])

students1 = [
    [10, 'Peter', 25, 3.1], 
    [11, 'Mary', 23, 3.5],
    [12, 'Nick', 21, 3.2]
]

students2 = [
    {'id': 10, 'name': 'Peter', 'age': 25, 'gpa': 3.1}, 
    {'id': 11, 'name': 'Mary', 'age': 23, 'gpa': 3.5}, 
    {'id': 12, 'name': 'Nick', 'age': 21, 'gpa': 3.2}, 
]

for student in students2:
    print(student['name'])

students3 = {
    10: {'id': 10, 'name': 'Peter', 'age': 25, 'gpa': 3.1}, 
    11: {'id': 11, 'name': 'Mary', 'age': 23, 'gpa': 3.5}, 
    12: {'id': 12, 'name': 'Nick', 'age': 21, 'gpa': 3.2}, 
}

s = students3[11]
print(s)