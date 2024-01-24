from sys import stdin

def main():
    n, m = map(int, input().split())

    d = dict()
    for _ in range(n):
        site, password = stdin.readline().rstrip().split()
        d[site] = password

    for _ in range(m):
        site = stdin.readline().rstrip()
        print(d[site])

main()