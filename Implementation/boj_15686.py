from itertools import combinations


def solution():
    n,m = map(int, input().split())

    board = []

    house = []
    chicken_house = []

    for i in range(n):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(len(line)):
            if line[j] == 1:
                house.append((i, j))
            if line[j] == 2:
                chicken_house.append((i, j))

    chicken_combi = combinations(chicken_house, m)

    result = 100000
    for combi in chicken_combi:
        chicken_distance_of_combi = 0
        for h in house:
            min_distance = 100
            for c in combi:
                distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
                min_distance = min(min_distance, distance)
            chicken_distance_of_combi += min_distance
        result = min(result, chicken_distance_of_combi)

    return result


def main():
    print(solution())


if __name__ == '__main__':
    main()
