def Race(A,B,C):
    if  abs(C-B) < abs(C-A):
        return("S")
    elif abs(C-B) > abs(C-A):
        return("N")
    else:
        return("D")