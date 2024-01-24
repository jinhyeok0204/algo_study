# 수들의 합
# Two Pointer, Prefix Sum
n, m = map(int, input().split())

ary = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for i in ary:
    sum_value += i
    prefix_sum.append(sum_value)

count = 0
# 부분합 =  P[R] - P[L-1]

left = 0
right = 1

while left <= right:

    if right >= n+1:
        break
    value = prefix_sum[right] - prefix_sum[left]

    if value == m:
        count += 1
        left += 1

    elif value < m:
        right += 1
    else:
        left += 1

print(count)

