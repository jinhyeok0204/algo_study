from itertools import combinations
from sys import stdin

# 비둘기 집 원리 !!

def main():
    t = int(input())
    for _ in range(t):
        print(solution())


def solution():
    n = int(input())
    mbti = stdin.readline().rstrip().split()
    if n > 32:
        return 0
    combi = set(list(combinations(mbti, 3)))

    result = 100000
    for c in combi:
        result = min(calc_distance_of_three_person(c), result)

    return result


def calc_distance_of_three_person(c: tuple[str, str, str]) -> int:
    distance = 0
    combi_of_two = combinations(c,2)

    for combi in combi_of_two:
        p1, p2 = combi
        distance += calc_distance(p1, p2)

    return distance


def calc_distance(p1: str, p2: str) -> int:
    distance = 0

    for i, j in zip(p1, p2):
        if i != j:
            distance += 1
    return distance


main()