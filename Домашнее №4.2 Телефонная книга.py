# Считываем количество записей
count_record = int(input())

# Создаем пустой словарь для хранения контактов
number_book = {}

# Заполняем словарь N раз
for _ in range(count_record):
    # Считываем строку, разделяем ее на имя и телефон по пробелу
    name, phone = input().split()
    # Сохраняем в словарь (так как имена уникальны, проверки не нужны)
    number_book[name] = phone

# Считываем имя контакта для поиска
search_name = input()

# Ищем контакт в словаре и выводим результат
if search_name in number_book:
    print(number_book[search_name])
else:
    print("Контакты не найдены")
