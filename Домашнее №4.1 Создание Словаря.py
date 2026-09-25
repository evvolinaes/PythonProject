keys = input().lower().split()
values = input().lower().split()

words = dict(zip(keys, values))
print(words)
#for key, values in words.items():
   # print(f"{key} : {values}")