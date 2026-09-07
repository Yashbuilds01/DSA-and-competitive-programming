N = int(input())
arr = list(map(int, input().split()))

freq = [0] * 101

for num in arr:
    freq[num] += 1

max_freq = 0
answer = 0

for num in range(1, 101):
    if freq[num] >= max_freq:
        max_freq = freq[num]
        answer = num

print(answer)