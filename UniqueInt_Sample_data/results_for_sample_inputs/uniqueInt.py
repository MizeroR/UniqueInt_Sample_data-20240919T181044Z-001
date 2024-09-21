max_int = 2 ** 31 - 1
min_int = -2 ** 31 + 1

unique_int = set()

with open ("input.txt" , "r") as file:
    for line in file:
        line = line.strip()

        try:
            my_int = int(line)

            if min_int <= my_int <= max_int:
                unique_int.add(my_int)
        except ValueError:
            continue
sorted_int = sorted(unique_int)

with open('output.txt' , 'w') as output_file:
    for my_int in sorted_int:
        output_file.write(f"{my_int}\n")