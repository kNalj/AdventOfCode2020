def get_num_trees(hor, ver):
    vertical_pos = 0
    horizontal_pos = 0
    matrix = []
    total = 0

    with open("input03") as file:
        for line in file:
            matrix.append(line.strip("\n"))
            # if line[horizontal_pos % len(line.strip("\n"))] == "#":
            #     total += 1
            # horizontal_pos += hor
            # vertical_pos += ver

    while vertical_pos < len(matrix):
        if matrix[vertical_pos][horizontal_pos % len(matrix[vertical_pos])] == "#":
            total += 1
        horizontal_pos += hor
        vertical_pos += ver

    return total

print(get_num_trees(1, 1) * get_num_trees(3, 1) * get_num_trees(5, 1) * get_num_trees(7, 1) * get_num_trees(1, 2))
