def main():
    n = int(input())

    d = [-1] * (n+1)
    if n >= 3:
        d[3] = 1
    if n >= 5:
        d[5] = 1

    for i in range(6, n+1):
        a = d[i-3]
        b = d[i-5]

        if a == -1 and b == -1:
            d[i] = -1
        elif a == -1 and b != -1:
            d[i] = b + 1
        elif a != -1 and b == -1:
            d[i] = a + 1
        else:
            d[i] = min(a,b) + 1

    print(d[n])

main()