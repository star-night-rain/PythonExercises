f = open("data.csv", "r")
for line in f:
    line = line.replace("\n", "")
    ls = line.split(",")
    ls.reverse()
    print(",".join(ls))
f.close()