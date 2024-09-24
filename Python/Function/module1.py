def add(a, b):
    return f"{a} + {b} = {a + b}"


def count_number(a, b):
    count = 0
    while a:
        if b == a.pop():
            count += 1
    return f"The number {b} appear {count} times in the list"


def time_transform(a, b):
    if a > 12:
        print(f"TIME: {a - 12}:{b} PM")
    else:
        print(f"TIME: {a}:{b} AM")


def ride(a, b):
    return f"{a} * {b} = {a * b}"
