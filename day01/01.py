input_data = []
with open("input01") as file:
    for line in file:
        input_data.append(int(line))

print(input_data)


def find(data):
    for i in data:
        for j in data:
            if i+j == 2020:
                return i*j


def find_three(data):
    for i in data:
        for j in data:
            for k in data:
                if i+j+k == 2020:
                    return i*j*k


print(find(input_data))
print(find_three(input_data))