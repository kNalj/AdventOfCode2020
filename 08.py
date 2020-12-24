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

executed = [False for _ in range(len(stack))]
alter = [False for _ in range(len(stack))]

no_repeats = True
alternate = False
return_index = 0

while no_repeats:
    instruction, parameter = stack[index].split(" ")
    if instruction == "nop":
        if alternate == False:
            return_index = index
            index += int(parameter)
            alternate = True
        else:
            index += 1
    elif instruction == "acc":
        index += 1
        acc += int(parameter)
    else:
        if alternate == False:
            return_index = index
            index += 1
            alternate = True
        else:
            index += int(parameter)

    if executed[index]:
        alternate = False
        index = return_index
    else:
        executed[index] = True


print(acc)