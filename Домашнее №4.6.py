import re

def mask_card_number(card: str) -> str:
    # Функция внутри заменяет каждую из первых 12 цифр на звёздочку
    # Регулярное выражение ищет цифру, если после неё в строке есть ещё как минимум 4 цифры
    return re.sub(r'\d(?=.*\d.*\d.*\d.*\d)', '*', card)

# Пример использования:
card_input = input("Введите номер карты: ")
print(mask_card_number(card_input))
