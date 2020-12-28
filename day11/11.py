data = []

with open("input11") as file:
    for line in file:
        data.append(line.strip("\n"))

print(data)


def check_adjecent(x, y, data):

    if x == 0:
        if y == 0:
            adjecents = [data[x][y + 1], data[x + 1][y], data[x + 1][y + 1]]
        elif y == len(data[0]) - 1:
            adjecents = [data[x][y - 1], data[x + 1][y - 1], data[x + 1][y]]
        else:
            adjecents = [data[x][y - 1], data[x][y + 1], data[x + 1][y - 1], data[x + 1][y], data[x + 1][y + 1]]
    elif y == 0:
        if x == len(data) - 1:
            adjecents = [data[x - 1][y], data[x - 1][y + 1], data[x][y + 1]]
        else:
            adjecents = [data[x - 1][y], data[x - 1][y + 1], data[x][y + 1], data[x + 1][y], data[x + 1][y + 1]]
    elif y == len(data[0]) - 1:
        if x == len(data) - 1:
            adjecents = [data[x - 1][y - 1], data[x - 1][y], data[x][y - 1]]
        else:
            adjecents = [data[x - 1][y - 1], data[x - 1][y], data[x][y - 1], data[x + 1][y - 1], data[x + 1][y]]
    elif x == len(data) - 1:
        adjecents = [data[x - 1][y - 1], data[x - 1][y], data[x - 1][y + 1], data[x][y - 1], data[x][y + 1]]
    else:
        adjecents = [data[x - 1][y - 1], data[x - 1][y], data[x - 1][y + 1],
                     data[x][y - 1], data[x][y + 1],
                     data[x + 1][y - 1], data[x + 1][y], data[x + 1][y + 1]]

    free, occupied = 0, 0
    for seat in adjecents:
        if seat == "#":
            occupied += 1
        elif seat == "L":
            free += 1

    return free, occupied


def update_seats(data):
    new_seating = data.copy()
    for i in range(len(data)):
        for j in range(len(data[0])):
            print(data[i][j], check_adjecent(i, j, data))
            if data[i][j] == "L" and check_adjecent(i, j, data)[1] == 0:
                new_seating[i] = new_seating[i][:j] + "#" + new_seating[i][j + 1:]
            elif data[i][j] == "#" and check_adjecent(i, j, data)[1] >= 4:
                new_seating[i] = new_seating[i][:j] + "L" + new_seating[i][j + 1:]

    return new_seating

not_same = True
while not_same:
    new_seating = update_seats(data)
    not_same = False
    for i in data:
        if i not in new_seating:
            not_same = True
    data = new_seating

total = 0
for i in data:
    for j in i:
        if j == "#":
            total += 1

print(total)


def check_directions(i, j, data):
    pass