
file = open("week05-functions/data.csv", "a")

id = input("ID: ")
name = input("Name: ")
age = input("Age: ")
gpa = input("GPA: ")

record = f"{id},{name},{age},{gpa}\n"

file.write(record)
file.close()