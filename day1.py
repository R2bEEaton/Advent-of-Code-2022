data = []

with open("day1input.txt") as f:
    total = 0
    for line in f.readlines():
        if line == "\n":
            data.append(total)
            total = 0
        else:
            total += int(line)

# Part 1
print(max(data))

# Part 2
print(sum(sorted(data)[-3:]))
