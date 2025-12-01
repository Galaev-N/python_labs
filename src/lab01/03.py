# Задание 3

price = float(input())
discount = float(input())
vat = float(input())

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

ans1 = f"База после скидки: {base:.2f} ₽"
ans2 = f"НДС: {vat_amount:.2f} ₽"
ans3 = f"Итого к оплате: {total:.2f} ₽"

print(f"{ans1:>27}")
print(f"{ans2:>27}")
print(f"{ans3:>27}")
