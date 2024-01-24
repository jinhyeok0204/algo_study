# 타일링 문제 -> dp의 대표 문제
def main():
    n = int(input())
    d = [0] * (n+1)
    d[0], d[1] = 1, 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2] * 2

    result = d[n] % 10007
    print(result)


if __name__ == '__main__':
    main()
