from collections import Counter


def solution(have, case):

    counter = Counter(have)

    result = []

    for t in case:
        if t in counter.keys():
            result.append(counter[t])
        else:
            result.append(0)
    return result


if __name__ == '__main__':
    n = int(input())
    have = list(map(int, input().split()))

    m = int(input())
    case = list(map(int, input().split()))

    print(*solution(have, case))