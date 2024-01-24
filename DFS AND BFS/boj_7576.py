from collections import deque


def main():
    m, n = map(int, input().split())

    box = []
    tomato = []
    for i in range(n):
        line = list(map(int, input().split()))
        box.append(line)

        for j in range(m):
            if line[j] == 1:
                tomato.append((i, j, 1))

    if no_zero(box):
        return 0

    q = deque(tomato)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    result_day = 1
    while q:

        y, x, day = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if box[ny][nx] in (-1, 1):
                continue

            box[ny][nx] = 1
            q.append((ny, nx, day+1))
            result_day = max(day, result_day)

    return result_day if no_zero(box) else -1


def no_zero(box):
    for line in box:
        for e in line:
            if e == 0:
                return False
    return True


if __name__ == '__main__':
    print(main())
