import sys


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    rec = []
    for _ in range(n):
        line = input().rstrip()
        to_append = []
        for each in line:
            to_append.append(int(each))
        rec.append(to_append)

    max_size = min(n,m)

    for size in range(max_size, 0, -1):
        for i in range(n-size+1):
            for j in range(m-size+1):
                if rec[i][j] == rec[i][j+size-1] == rec[i+size-1][j] == rec[i+size-1][j+size-1]:
                    print(size * size)
                    return


if __name__ == '__main__':
    main()