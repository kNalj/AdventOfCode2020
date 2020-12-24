import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]


def check_valid_passport(data, extra=False):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    fields = {field.split(":")[0]: field.split(":")[1] for field in data.split(" ")}
    for req_key in required:
        if req_key not in fields.keys():
            return False

    if extra:
        if int(fields["byr"]) > 2002 or int(fields["byr"]) < 1920:
            return False
        if int(fields["iyr"]) > 2020 or int(fields["iyr"]) < 2010:
            return False
        if int(fields["eyr"]) > 2030 or int(fields["eyr"]) < 2020:
            return False
        if fields["hgt"].endswith("cm"):
            if int(fields["hgt"].strip("cm")) < 150 or int(fields["hgt"].strip("cm")) > 193:
                return False
        elif fields["hgt"].endswith("in"):
            if int(fields["hgt"].strip("in")) > 76 or int(fields["hgt"].strip("in")) < 59:
                return False
        else:
            return False
        if not re.search(r'^#([0-9a-fA-F]{6})', fields["hcl"]):
            return False
        if fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if not re.search("^\d{9}$", fields["pid"]):
            return False

    return True


passports = []
with open("input04") as file:
    data = ""
    for line in file:
        if line == "\n":
            passports.append(data)
            data = ""
            continue
        if data == "":
            data += line.strip("\n")
        else:
            data += " " + line.strip("\n")
        if line == "\n":
            passports.append(data)
            data = ""
    passports.append(data)
total = 0
for passport in passports:
    if check_valid_passport(passport, extra=True):
        total += 1
    # else:
    #     print(passport)

print("Total: ", total)
