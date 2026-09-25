count_record = int(input())

synonym = {}

for _ in range(count_record):
    word1, word2 = input().split()
    # Записываем обе пары, чтобы поиск работал в обе стороны
    synonym[word1] = word2
    synonym[word2] = word1

search_name = input()

# Так как гарантируется, что слово есть в словаре, мы можем просто вывести его синоним
print(synonym[search_name])