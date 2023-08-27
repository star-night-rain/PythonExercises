for i in range(1000,10000):
    s = str(i)
    if pow(eval(s[0]),4)+pow(eval(s[1]),4)+\
        pow(eval(s[2]),4)+pow(eval(s[3]),4)\
        == i:
        print(i)