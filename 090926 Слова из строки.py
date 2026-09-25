import re

text = "Привет, как у тебя дела?" #input()
template_words = r"[А-Яа-я]+"

words = re.findall(template_words, text)
#first_word = words[0]
two_letters = r"\b[А-Яа-я]{1,2}"
result = re.findall(two_letters, text)
print(result)
#2ая часть задачи Первые две буквы каждого слова
#for word in words:
   # print(words[:2])
#print(first_words)


