words = input().split()

found_word = None
for word in words:
    if word.startswith('б') or word.startswith('Б'):
        found_word = word
        break
if found_word:
    print(found_word)
else:
    print("слов на б нет")
