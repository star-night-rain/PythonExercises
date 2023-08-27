f = open("data.csv", "r")
for line in f.readlines():
    line = line.replace(" ","")
    print(line,end = "")
f.close()