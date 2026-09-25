words = input().lower().split()

words_count = {}
for word in words:
    if word in words_count:
        words_count[word] +=1
    else:
        words_count[word] = 1

#print(words_count)

for key, value in words_count.items():
    print(f"{key}: {value}")


