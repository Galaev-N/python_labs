# Задание С

def format_record(tuuple):
    # Реализуем обработку фамилии
    fio = tuuple[0].split()
    m = len(fio) - 1
    fio_str = f'{fio[0][0].upper()}{fio[0][1:]} '
    for i in range(1, m+1):
        fio_str += f'{fio[i][0].upper()}.'
    fio_str += ','

    # Реализуем обработку группы
    group_str = f' гр. {tuuple[1]},'

    # Реализуем обработку GPA(че это (средний балл успеваемости))
    GPA_str = f' GPA {tuuple[2]:.2f}'

    return fio_str + group_str + GPA_str
#print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
