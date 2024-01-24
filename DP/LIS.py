# LIS (가장 긴 증가하는 부분 수열)
# boj 11053
def main():
    n = int(input())
    ary = list(map(int, input().split()))
    d = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if ary[i] > ary[j]:
                d[i] = max(d[i], d[j] + 1)
    print(max(d))


if __name__ == '__main__':
    main()
    