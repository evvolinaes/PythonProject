word = "привет"
consonats = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ".lower()
letters = [letter*2 for letter in word if letter in consonats]
print(letters)