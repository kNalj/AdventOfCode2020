import time


class State:
    def __init__(self, index, acc, visited):
        self.index = index
        self.acc = acc
        self.visited = visited

    def get_state(self):
        return self.index, self.acc, self.visited


stack = []
acc = 0
index = 0


with open("input08") as file:
    for line in file:
        command = line.strip("\n")
        stack.append(command)

executed = [False for _ in range(len(stack))]
no_repeats = True

while no_repeats:
    instruction, parameter = stack[index].split(" ")
    if instruction == "nop":
        index += 1
    elif instruction == "acc":
        index += 1
        acc += int(parameter)
    else:
        index += int(parameter)

    if executed[index]:
        break
    else:
        executed[index] = True

print(acc)

acc = 0
index = 0
changed = False
visited = [False for _ in range(len(stack))]
visited[0] = True
state = State(index, acc, visited)

while index < len(stack):
    instruction, parameter = stack[index].split(" ")
    # print(index, instruction, parameter)

    if not changed:
        state = State(index, acc, visited)
        if instruction == "nop":
            visited[index] = True
            index += int(parameter)
        elif instruction == "acc":
            visited[index] = True
            index += 1
            acc += int(parameter)
        else:
            visited[index] = True
            index += 1
        changed = True
    else:
        if instruction == "nop":
            visited[index] = True
            index += 1
        elif instruction == "acc":
            visited[index] = True
            index += 1
            acc += int(parameter)
        else:
            visited[index] = True
            index += int(parameter)

    if index > len(stack) - 1:
        break
    if visited[index]:
        # print(index, acc)
        # print("RETURNING")
        # print(state.get_state())
        changed = False
        index, acc, visited = state.get_state()
        instruction, parameter = stack[index].split(" ")
        if instruction == "nop":
            visited[index] = True
            index += 1
        elif instruction == "acc":
            visited[index] = True
            index += 1
            acc += int(parameter)
        else:
            visited[index] = True
            index += int(parameter)


print("Acc", acc)