def print_pattern(rows):
    num_elements = sum([2 * (rows - i) - 1 for i in range(rows)])
    current = 2 * num_elements - 1

    for i in range(rows):
        spaces = "   " * i
        count = 2 * (rows - i) - 1
        row = []
        for _ in range(count):
            row.append(str(current))
            current -= 2
        print(spaces + " ".join(row))

n = int(input("Enter number of rows: "))
print_pattern(n)