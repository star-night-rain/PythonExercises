def prime(m):
    for i in range(2,m):
        if m%i == 0:
            return False
    return True
n = eval(input())
if int(n) - n == 0:
    m=n
else:
    m=int(n)+1
s=''
for i in range(5):
    while(not prime(m)):
        m+=1
    s+=(str(m)+',')
    m+=1
print(s[:-1])