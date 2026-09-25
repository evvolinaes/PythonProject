import re

#password = "nWd7pass"
password = "12WERё522"
correct_password = r"(?=.*[a-za-я])(?=.*[A-ZA-Я])(?=.*\d)" # - ?= - просматриваем группу, сначала просматриваем строку
result = re.match(correct_password, password)
print(bool(result))
#1. Длина >8
r"{8,}"
#2. Есть маленькая буква
r".*[а-za-я]"
#3. Есть большая буква
r".*[A-ZA-Я]"
#4. Есть большая буква
r".*\d"