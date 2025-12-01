# Задание 7

chifre = input("in: ")
word = ""
first_letter_index = 0
second_letter_index = 0
answer = ""
for i in chifre:
    if i.upper() == i:
        word += i
        first_letter_index = chifre.index(word)
        break
for j in chifre:
    if j.isdigit() == 1:
        second_letter_index = chifre.index(j) + 1
        word += chifre[second_letter_index]
        break
for k in range(
    first_letter_index, len(chifre), second_letter_index - first_letter_index
):
    answer += chifre[k]
print(f"out: {answer}")
