# Day 1
| | Time |
|---|---|
|Part 1|2:09|
|Part 2|1:39|
|Total|3:48|

```python
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
```
