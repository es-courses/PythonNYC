import csv 

file = open("week05-functions/data.csv")

data = csv.DictReader(file) 

for student in data:
    print(student['name'])
