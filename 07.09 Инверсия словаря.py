student_marks = {
    "Анна": 4,
    "Петр": 3,
    "Алекс": 5,
    "Иван": 5,
    "Ольга": 4,
    "Илья": 4,
    "Василий": 3,

}
marks = {}
for name, mark in student_marks.items():
    if mark in marks:
        marks[mark].append(name)
    else:
        marks[mark] = [name]
print(marks)

#То что должны получить:
# marks = {
#     4: ["Анна", "ольга"],
#     5: ["Алекс", "Иван"],
#     3: ["Петр"],
# }