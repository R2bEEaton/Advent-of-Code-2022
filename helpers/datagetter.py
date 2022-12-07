import keyboard
import re
import aocd


with open("sess") as f:
    sess = f.readline()


def data_in(day, split=True, numbers=False):
    print("Waiting for key...")
    key = keyboard.read_key()

    if key == 'ctrl':
        data = open("testdata1.txt").read()
    elif key == 'shift':
        data = open("testdata2.txt").read()
    else:
        data = aocd.get_data(session=sess, day=day)

    # Parse
    if split:
        data = data.split("\n")
    if numbers:
        out = []
        for line in (data if type(data) == list else data.split("\n")):
            out.append(get_numbers(line))
        data = out

    return data


def submit(ans):
    aocd.submit(answer=ans, session=sess)


def get_numbers(a):
    return list(map(float, re.findall(r'\d+(?:\.\d+)?', a)))
