word = "привет"
#мы хотим перебрать все элементы и сложить их в строку. Если орачиваем в строку в список, то получим список из букв
print(list(word))
#теперь хотим получить список, затем внутри используем цикл word с помощью list comprehensions
letters = [letter+"!" for letter in word]
print(letters)

