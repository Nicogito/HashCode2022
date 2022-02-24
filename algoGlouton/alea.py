f = open("input_5.txt", "r")
lines=f.readlines()
f.close()
lines.pop(0)

for i in range(len(lines)):
    lines[i]= lines[i].split(",")
    for j in range(len(lines[i])):
        lines[i][j]=int(lines[i][j])