string = input()

#str.lower() преобразуем из множества для отбрасывания дубликатов
string = string.lower()
string = string.replace(" ", "")
#str -> list[] преобразуем в список
words = string.split(',')
#print(words)
#list -> set{} преобразуемв множество
uniq_words = set(words)
#print(uniq_words)
#len(set)
print(len(uniq_words))