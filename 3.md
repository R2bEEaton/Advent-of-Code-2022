# Day 3
| | Part 1 | Part 2 | Total |
|---|---|---|---|
|Time|5:56|2:15|8:11|

```python
import aocd
with open("sess") as f:
    sess = f.readline()
din = aocd.get_data(session=sess, year=2022, day=3).split("\n")

# Part 1
s = 0
for line in din:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    for char in first:
        if char in second:
            if char.isupper():
                s += ord(char)-38
            else:
                s += ord(char)-96
            break

print(s)

# Part 2
s = 0
for i in range(0, len(din), 3):
    first = din[i]
    second = din[i+1]
    third = din[i+2]

    both = []
    for thing in first:
        if thing in second:
            both.append(thing)

    for char in both:
        if char in third:
            if char.isupper():
                s += ord(char) - 38
            else:
                s += ord(char) - 96
            break

print(s)
```
