import time

numbers = []
valid = False

with open("input09") as file:
    for line in file:
        numbers.append(int(line.strip("\n")))

for i in range(25, len(numbers)):
    valid = False
    for j in numbers[i-25:i]:
        for k in numbers[i - 25:i]:
            if j + k == numbers[i]:
                valid = True
                break
        if valid:
            break
    if not valid:
        break

print(numbers[i])

total = 0
start = 0
while total < numbers[i]:

    for l in range(start, len(numbers)):
        total += numbers[l]
        if total == numbers[i]:
            low = start
            high = l
            break
        elif total > numbers[i]:
            total = 0
            start += 1
            break


mini = min(numbers[low:high+1])
maxi = max(numbers[low:high+1])

print(mini + maxi)