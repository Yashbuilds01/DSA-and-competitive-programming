N= int(input())
string="a"
for i in range(0,N-1):
    if string[len(string)-1]=="b":
        string= string+ "a"
    else:
        string = string + "b"
print(string)