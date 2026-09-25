word = "привет"
consonats = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ".lower()
#letters = [letter*2 for letter in word if letter in consonats]
letters = []
for letter in word:
    if letter in consonats:
        letters.append(letter*2)
print(letters)
