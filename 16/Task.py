# file = open("data.txt", "r", encoding="utf-8")
#
# for line in file:
#     print(line.strip())
#
# file.close()

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        int(line.strip())


ddsg
