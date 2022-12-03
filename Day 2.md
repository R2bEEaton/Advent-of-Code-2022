# Day 2

| | Part 1 | Part 2 | Total |
|---|---|---|---|
|Time|13:17|13:08|26:25|

```python
import aocd
with open("sess") as f:
    sess = f.readline()
din = aocd.get_data(session=sess, year=2022, day=2).split("\n")

plays = ['A', 'B', 'C']
oppplays = ['X', 'Y', 'Z']
score = 0

# I lost my Part 1 code but it was terrible so that's fine
# This all took me way too long. I was struggling with obo errors
# and not thinking well.

for elem in din:
    a = plays.index(elem[0])
    b = oppplays.index(elem[2])

    if b == 2:
        score += ((a + 1) % 3) + 6 + 1
    elif b == 1:
        score += a + 3 + 1
    else:
        score += (a - 1) % 3 + 1

print(score)
```
