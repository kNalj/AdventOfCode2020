total = 0
total_2 = 0
with open("input02") as file:
    for line in file:
        [rule, password] = line.split(":")
        [numbers, letter] = rule.split(" ")
        [minn, maxn] = numbers.split("-")
        minn = int(minn)
        maxn = int(maxn)

        if minn <= password.count(letter) and password.count(letter) <= maxn:
            total += 1

        if password[minn] != password[maxn] and letter in [password[minn], password[maxn]]:
            total_2 += 1

print(total)
print(total_2)
