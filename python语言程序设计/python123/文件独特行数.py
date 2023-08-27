f = open("latex.log", "r")
ls = f.readlines()
f.close()
s = set(ls)
for i in s:
    ls.remove(i)
t = set(ls)
print("共{}独特行".format(len(s)-len(t)))