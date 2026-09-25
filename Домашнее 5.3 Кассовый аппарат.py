file = open("sold.txt", "r", encoding="utf-8")

summa_product = 0
max_initial = None
min_initial = None

for line in file:
    number = list(map(float, line.split()))
    summa_product += sum(number)

    if max_initial is None:
        max_initial = max(number)
        min_initial = min(number)
    else:
        max_initial = max(max_initial, max(number))
        min_initial = min(min_initial, min(number))

file.close()
print(f"{summa_product:.2f}")
print(f"{max_initial:.2f}")
print(f"{min_initial:.2f}")
