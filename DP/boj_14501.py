def main():
    n = int(input())
    t = []
    p = []
    for i in range(n):
        time, pay = map(int, input().split())
        t.append(time)
        p.append(pay)

    d = [0] * (n+1)
    # d[i]는 i일 이후에 얻을 수 있는 최대 이익
    max_value = 0
    for i in range(n - 1, -1, -1):
        time = t[i] + i
        if time <= n:
            d[i] = max(p[i] + d[time], max_value)
            max_value = d[i]
        else:
            d[i] = max_value
    print(max_value)

main()