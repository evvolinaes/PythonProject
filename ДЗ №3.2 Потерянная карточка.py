n = int(input())
remaining_numbers = []
sum_card = 0

while len(remaining_numbers) < n - 1:
    card = int(input())
    remaining_numbers.append(card)
    sum_card += card

ideal_sum = n * (n+1) // 2
lost_card = ideal_sum - sum_card

print(lost_card)


