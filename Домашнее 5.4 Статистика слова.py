def get_word_stats(word):

    vowels = "АЕЁИОУЫЭЮЯ".lower()
    consonats = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ".lower()
    count_consonants = 0
    count_vowels = 0

    for letter in word.lower():
        if letter in vowels:
            count_vowels += 1
        elif letter in consonats:
            count_consonants += 1


    length_word = len(word)
    return length_word, count_vowels,  count_consonants

print(get_word_stats("буква"))






