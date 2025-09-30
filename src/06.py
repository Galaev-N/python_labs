# Задние 6

N = int(input('in_1: '))
count = 0
for i in range(1, N+1):
    name, second_name, age, och = input(f'in_{i+1}: ').split()
    if och == 'True': count += 1
print(f'out: {count} {N - count}')
