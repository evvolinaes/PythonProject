import re

# 1. Считываем текст и приводим его к нижнему регистру
text = input().lower()

# 2. Находим все слова (последовательности букв) в тексте
words = re.findall(r'[a-zа-яё]+', text)

# 3. Считаем частоту каждого слова с помощью обычного словаря
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# 4. Находим лучшее слово: сначала по убыванию частоты (-word_counts[w]),
# а при равенстве частот — по алфавиту (w)
best_word = min(word_counts.keys(), key=lambda w: (-word_counts[w], w))

# 5. Выводим результат
print(best_word)