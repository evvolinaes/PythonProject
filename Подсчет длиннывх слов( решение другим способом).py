text = input()
#text = "привет как настроение"
#words = text.split() #преобразовали строку в список
#print(len([word for word in text.split() if len(word)>5])) #с помощью списочного выражения

#тоже через списочный только упрощенно , разгрузив длинную строку:
word = text.split()
long_words = [word for word in words if len(word) > 5]
print(len(long_words))



#num_longest_word = 0 #количество длинных слов
#for word in words:
    #if len(word)>5:
       # num_longest_word +=1

#print(num_longest_word)
