"""
    n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다. 이때 이 수열에서 x가 등장하는 횟수를 구하라.
    단, 이 문제는 시간 복잡도 O(logN)으로 설계해야 한다.

    예시)
    7 2
    1 1 2 2 2 2 3
    에서 2가 나온 횟수가 4이므로 답은 4이다.
"""

import sys
import bisect


def main():
    input = sys.stdin.readline
    n, x = map(int, input().split())

    numbers = list(map(int, input().split()))

    result_1 = solution_1(n, numbers, x)
    result_2 = solution_2(numbers, x)

    assert(result_1 == result_2)
    print(result_1)

def solution_1(n, numbers, target):

    last_idx = get_last_idx(n, numbers, target, 0, n - 1)
    first_idx = get_first_idx(numbers, target, 0, n - 1)

    return last_idx - first_idx + 1


def get_first_idx(numbers, target, start, end) -> None or int:

    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or target > numbers[mid - 1]) and numbers[mid] == target:
        return mid
    elif numbers[mid] >= target:
        return get_first_idx(numbers, target, start, mid-1)
    else:
        return get_first_idx(numbers, target, mid + 1, end)


def get_last_idx(n, numbers, target, start, end) -> None or int:

    if start > end:
        return None

    mid = (start + end) // 2
    if (mid == n - 1 or target < numbers[mid+1]) and numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        return get_last_idx(n, numbers, target, start, mid - 1)
    else:
        return get_last_idx(n, numbers, target, mid + 1, end)


def solution_2(numbers: list, target: int) -> int:

    last_idx = bisect.bisect_right(numbers, target)
    first_idx = bisect.bisect_left(numbers, target)

    return last_idx - first_idx


main()