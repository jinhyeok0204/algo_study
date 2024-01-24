from sys import stdin
from collections import deque


def solution():
    funcs = stdin.readline().rstrip()
    n = int(input())
    s = stdin.readline().rstrip()
    ary = deque(s[1:-1].split(",")) if s != '[]' else deque()

    is_reversed = False
    for f in funcs:
        if f == "R":
            is_reversed = not is_reversed
        elif f == "D":
            if len(ary) < 1:
                return "error"
            if is_reversed:
                ary.pop()
            else:
                ary.popleft()

    if is_reversed:
        ary.reverse()

    return ary


def main():
    t = int(input())
    for _ in range(t):
        result = solution()
        result = list(result) if result != "error" else "error"

        if result == "error":
            print("error")
        else:
            print("[" + ",".join(result) + "]")


if __name__ == '__main__':
    main()
