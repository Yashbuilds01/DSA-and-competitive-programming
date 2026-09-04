import math

N = int(input())
A = list(map(int, input().split()))

sum_of_squares = 0

for x in A:
    sum_of_squares += x * x

mean = sum_of_squares / N
rms = math.sqrt(mean)

print(f"{rms:.6f}")