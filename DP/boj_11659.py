import sys

def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    nums = list(map(int, sys.stdin.readline().rstrip().split()))

    d = [0] * (n+1)
    for i in range(1, n+1):
        d[i] = d[i-1] + nums[i-1]

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        result = d[j] - d[i-1]
        print(result)


if __name__ == '__main__':
    main()