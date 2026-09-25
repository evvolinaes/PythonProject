with open("salaries.txt", "r", encoding="utf-8") as file_in, open(
        "highly_paid.txt", "w", encoding="utf-8"
) as file_out:
    header = file_in.readline()
    for line in file_in:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) >= 4:
            last_name = parts[0]
            first_name = parts[1]
            patronymic = parts[2]
            salary = int(parts[3])

            if salary > 60000:
                output_line = (
                    f"{last_name} {first_name[0]}.{patronymic[0]}. !\n")
            file_out.write(output_line)