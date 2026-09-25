words = input().split("!")

#len_words = []
#for word in words:
    #len_words.append(len(word))

    #задача с помощью лист комприхеншионс
len_words = [len(word) for word in words]

print(len_words)
