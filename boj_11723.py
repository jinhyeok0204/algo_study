from sys import stdin
m = int(input())

s = set()

for _ in range(m):
    command = stdin.readline().rstrip().split()

    to_do = command[0]

    if to_do == "add":
        num = int(command[1])
        s.add(num)

    elif to_do == "remove":
        num = int(command[1])
        try:
            s.remove(num)
        except KeyError:
            continue

    elif to_do == "check":
        num = int(command[1])
        print(1) if num in s else print(0)

    elif to_do == "toggle":
        num = int(command[1])
        try:
            s.remove(num)
        except KeyError:
            s.add(num)

    elif to_do == "all":
        s = set(list(range(1, 21)))
    elif to_do == "empty":
        s = set()

