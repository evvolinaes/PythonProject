#print("hello", "hi", sep=", ", end="!")

data = {"c": 3, "a": 1, "b": 2}

sorted_dict = {key: data[key] for key in sorted(data.keys())}
print(sorted_dict)