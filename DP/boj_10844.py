# dp 테이블 => d[자릿수][앞에 오는 숫자] = 경우의 수
# 앞에 오는 숫자 = 0일때.
# d[자릿수][0] = d[자릿수 - 1][1]
def main():
    n = int(input())
    d = [[0] * 10 for _ in range(n+1)]

    for i in range(1, 10):
        d[1][i] = 1

    for i in range(2, n+1):
        for j in range(0, 10):
            if j == 0:
                d[i][j] = d[i-1][1]
            elif j == 9:
                d[i][j] = d[i-1][8]
            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]

    result = sum(d[n])
    print(result % 1000000000)


if __name__ == '__main__':
    main()


