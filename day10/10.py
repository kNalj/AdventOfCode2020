data = []

with open("input10") as file:
    for line in file:
        data.append(int(line.strip("\n")))

sort = [0] + sorted(data)

diffs = [0, 0, 0]
for i, value in enumerate(sort):
    if i > 0:
        diffs[value - sort[i-1] - 1] += 1

print((diffs[0] + 1) * (diffs[2] + 1))


# ######################### WOULD WORK BUT TOO SLOW ###################################################
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def get_children(self):
        l = []
        for child in self.children:
            l.append(child.value)
        return l


def create_node(node, list, start):
    if start >= len(list):
        return
    for item in list[start:start+3]:
        if (item - node.value <= 3) and (item - node.value > 0):
            node.children.append(Node(item))
    print(node.value, "-", node.get_children(), list[start:start+3])
    if node.children == []:
        return
    else:
        for i, item in enumerate(node.children):
            create_node(item, list, start+1+i)


def count_nodes(node):
    if node.children == []:
        return 1
    else:
        sum = 0
        for child in node.children:
            sum += count_nodes(child)

    return sum

# #####################################################################################################

results = [0 for _ in range(sort[-1] + 1)]
for i in range(sort[-1] + 1):
    if i == 0:
        results[i] = 1
    elif i == 1:
        results[i] = results[i-1]
    elif i == 2:
        results[i] = results[i-2] + results[i-1]
    else:
        results[i] = results[i-3] + results[i-2] + results[i-1]

    if i not in sort:
        results[i] = 0

print(results)
