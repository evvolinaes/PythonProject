file = open("numbers.txt", "r", encoding="utf-8")
sum_numbers = 0
count_num = 0

for line in file:
    number = int(line.strip())
    sum_numbers+= number
    count_num = count_num + 1
file.close()
arithmetic_mean = sum_numbers/count_num

print(f"{sum_numbers:.2f} {arithmetic_mean:.2f}")

