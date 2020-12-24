"""

--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms
are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for
which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each
of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the
same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane
(your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers
are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?


"""
data = []
with open("input06") as file:
    group = []
    for line in file:
        if line == "\n":
            data.append(group)
            group = []
            continue

        group.append(line.strip("\n"))
    data.append(group)

# part 1
flat_data = []
for group in data:
    newitem = ""
    for item in group:
        newitem += item
    flat_data.append(newitem)
total = 0
filtered = [set(group) for group in flat_data]
for i in filtered:
    total += len(i)
print("Total with 1 yes: {}".format(total))

# part 2
total = 0
for group in data:
    all_yes = set(group[0])
    for item in group:
        all_yes = all_yes & set(item)
    total += len(all_yes)
print("Total for all yes: {}".format(total))