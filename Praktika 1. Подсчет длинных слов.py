text = input()
#text = "привет как настроение"
words = text.split() #преобразовали строку в список

num_longest_word = 0 #количество длинных слов
for word in words:
    if len(word)>5:
        num_longest_word +=1

print(num_longest_word)
