def main():
    t = int(input())
    ls = []
    for _ in range(t):
        ls.append(solution())
    print(*ls)


def solution():
    # <m:n>이 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는가
    m, n, x, y = map(int, input().split())

    if m < n:
        small = m
        idx = 0
    else:
        

main()