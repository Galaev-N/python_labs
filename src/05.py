# Задание 5

fio = input('ФИО: ')

inits = fio.split()

print(f'Инициалы: {inits[0][0] + inits[1][0] + inits[2][0]}.')
print(f'Длина (символов): {len(inits[0]) + len(inits[1]) + len(inits[2]) + 2}')
