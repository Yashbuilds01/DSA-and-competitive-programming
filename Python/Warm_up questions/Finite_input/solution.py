lst =[]
while True:
    a = int(input())
    if a==0:
        lst.append(0)
        break
    lst.append(a)
print(' '.join(map(str, lst)))