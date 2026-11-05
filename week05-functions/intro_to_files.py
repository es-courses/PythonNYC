
file = open("week05-functions/data.txt", "r")

lines = file.readlines()
for line in lines:
    line = line.strip()
    print(line)

file.close()

file = open("week05-functions/data.txt", "a")
txt = input("Type a sentence: ")
file.write(txt + '\n')
file.close()