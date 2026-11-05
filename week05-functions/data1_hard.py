
file = open("week05-functions/data.csv")

lines = file.readlines()

for line in lines[1:]:
    parts = line.strip().split(',')
    print(f"{parts[1]}, {parts[3]}")