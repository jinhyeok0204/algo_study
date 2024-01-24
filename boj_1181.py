def main():
    n = int(input())
    s = set()

    for _ in range(n):
        s.add(input())

    ls = list(s)
    ls.sort()
    ls.sort(key=lambda x:len(x))

    for each in ls:
        print(each)


main()
