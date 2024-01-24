def main():
    n = int(input())
    for _ in range(n):
        s = input()
        result = is_vps(s)

        print("YES") if result else print("NO")


def is_vps(s: str) -> bool:
    ls = []
    for e in s:
        if e == "(":
            ls.append(e)

        elif e == ")":
            try:
                ls.pop()
            except IndexError:
                return False

    return True if len(ls) == 0 else False


if __name__ == '__main__':
    main()
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    nums.sort()