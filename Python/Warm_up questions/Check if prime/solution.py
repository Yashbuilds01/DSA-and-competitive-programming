from math import sqrt
T= int(input())
for i in range(0,T):
    a= int(input())
    if a <=1:
        print("No")
        continue
    is_prime = True
    initial =2 
    while initial <= sqrt(a) :
        if a % initial ==0:
            is_prime =False
            break
        initial +=1
    if not is_prime:
        print("No")
    else:
        print ("Yes")