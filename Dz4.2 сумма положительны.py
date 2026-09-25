string_list = input().split()
total_sum = 0
for iter in string_list:
    num = int(iter)
    if num > 0:
        total_sum += num

print(total_sum)