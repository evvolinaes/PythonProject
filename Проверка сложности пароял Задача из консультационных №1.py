#решение задачи без регулярного выражения
password = "mypassWord7"
# условия
# длина > 8
min_len = len(password) >= 8



#есть маленькая буква
has_small_letter = False
for letter in password:
    if letter.islower():
        has_small_letter = True

# большая буква
has_big_letter = False
for letter in password:
    if letter.isupper():
        has_big_letter = True



# есть цифра
has_number = False #изначально мы говорим что у нас нет цифры
for letter in password: #затем перебираем
    if letter.isdigit(): #если есть цифра выведи истину в переменной цикла
        has_number = True



if min_len and has_small_letter and has_big_letter and has_number:
    print("корректный")
else:
    print("Некорр")