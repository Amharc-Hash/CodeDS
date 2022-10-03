def num_grid(lst):
    for i in range(0, 5):
        for j in range(0, 5):
            if lst[i][j] == '-':
                lst[i][j] = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if lst[i][j] == '#':
                if i > 0 and isinstance(lst[i - 1][j], int): lst[i - 1][j] += 1
                if j < 4 and isinstance(lst[i][j + 1], int): lst[i][j + 1] += 1
                if j > 0 and isinstance(lst[i][j - 1], int): lst[i][j - 1] += 1
                if i < 4 and isinstance(lst[i + 1][j], int): lst[i + 1][j] += 1
                if i > 0 and j > 0 and isinstance(lst[i - 1][j - 1], int): lst[i - 1][j - 1] += 1
                if i > 0 and j < 4 and isinstance(lst[i - 1][j + 1], int): lst[i - 1][j + 1] += 1
                if i < 4 and j > 0 and isinstance(lst[i + 1][j - 1], int): lst[i + 1][j - 1] += 1
                if i < 4 and j < 4 and isinstance(lst[i + 1][j + 1], int): lst[i + 1][j + 1] += 1
    for i in range(0, 5):
        for j in range(0, 5):
            if isinstance(lst[i][j], int):
                lst[i][j] = str(lst[i][j])

    return lst


'''lst_input = [
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","#","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"]
]'''

lst_input = []
print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
    lst_input.append([i for i in e.split()])

print("\n", *lst_input, sep="\n")
print("\n", *num_grid(lst_input), sep="\n")
