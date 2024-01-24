k, n = map(int, input().split())

lan_cables = []
for _ in range(k):
    length = int(input())
    lan_cables.append(length)

start = 1
end = max(lan_cables)
result = 0
while start <= end:

    mid = (start + end) // 2

    made = 0
    for lan in lan_cables:
        made += (lan // mid)

    # 많이 만들어지거나 딱 맞게 만들어 졌을 때.. n개보다 많이 만든 것도 n개를 만드는 것에 포함됨
    if made >= n:
        if result < mid:
            result = mid
        start = mid + 1

    # 너무 적게 만들어짐
    elif made < n:
        end = mid - 1

print(result)
