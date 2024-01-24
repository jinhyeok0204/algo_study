# 계수 정렬은 데이터 크기가 제한되어 있을때 빠르게 동작한다.
# 시간복잡도, 공간복잡도 O(N+K)

import sys
input = sys.stdin.readline
n = int(input().rstrip())

nums = [0] * 10001
for _ in range(n):
    idx = int(input().rstrip())
    nums[idx] += 1

length = len(nums)
for i in range(length):
    for j in range(nums[i]):
        print(i)


while True:
    n = input()
    if n == "0":
        break

    if n.reverse() == n:
        print("yes")
    else:
        print("no")
