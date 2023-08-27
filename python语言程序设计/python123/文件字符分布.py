f= open("latex.log", "r")
counts = {}
sum = 0
for line in f:
    for c in line:
        counts[c] = counts.get(c, 0) + 1
        sum += 1
print("共{}字符".format(sum), end = "")
for i in range(26):
    if counts[chr(ord('a')+i)] != 0:
        print(",{}:{}".format(chr(ord("a")+i), counts[chr(ord('a')+i)]), end = '')