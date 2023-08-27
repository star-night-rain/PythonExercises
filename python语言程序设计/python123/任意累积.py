def cmul(*b):
    i = 1
    for j in b:
        i *= j
    return i
print(eval("cmul({})".format(input())))