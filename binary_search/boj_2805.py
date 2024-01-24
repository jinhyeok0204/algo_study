def main():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    h = 0
    start = 0
    end = max(trees)

    while start <= end:
        # 이게 H 후보
        mid = (start + end) // 2

        made = 0
        for t in trees:
            if t >= mid:
                made += (t - mid)

        # 적어도 M 미터를 가져가야한다.
        if made >= m:
            h = max(h, mid)
            start = mid + 1
        # 길이가 모자람.. h를 감소시켜야된다
        else:
            end = mid - 1
    print(h)

main()