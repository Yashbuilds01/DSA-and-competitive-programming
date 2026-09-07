import math
try:
    data=str(input())
    new_data=data.split(" ")
    first_no,second_no=new_data
    value=int(first_no)/ int(second_no)
    print(math.floor(value))
except ZeroDivisionError:
    print(-1)