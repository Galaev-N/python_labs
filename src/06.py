# Задние 6

N = int(input())
count = 0
for i in range(N):
    name, second_name, age, och = input().split()
    if och == 'True': count += 1
print(count, N - count)