from collections import deque


def main():
    m, n, h = map(int, input().split())
    box = [[] for _ in range(h)]  # list[list[list]] 박스 -> 층 -> 토마토 라인

    tomato = []  # (day, x, y, floor)
    for floor in range(h):
        for i in range(n):
            line = list(map(int, input().split()))
            box[floor].append(line)
            for j in range(m):
                if box[floor][i][j] == 1:
                    tomato.append((0, i, j, floor))

    day = dfs(m, n, h, box, tomato)

    print(day)


def dfs(m, n, h, box, tomato):

    if not have_zero(box):
        return 0

    q = deque(tomato)

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    dh = [1, -1]

    # 위 : dh = 1 dx = 0 dy = 0
    # 아래 : dh = -1, dx = 0, dy = 0
    # 왼, 오, 앞, 뒤

    max_day = 0

    while q:
        day, x, y, floor = q.popleft()

        if day > max_day:
            max_day = day

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if box[floor][nx][ny] == 0:
                q.append((day + 1, nx, ny, floor))
                box[floor][nx][ny] = 1

        for i in range(2):
            nh = floor + dh[i]

            if nh >= h or nh < 0:
                continue

            if box[nh][x][y] == 0:
                q.append((day + 1, x, y, nh))
                box[nh][x][y] = 1

    if have_zero(box):
        return -1

    return max_day


def have_zero(box: list[list[list]]):
    for floor in box:
        for line in floor:
            if 0 in line:
                return True
    return False


main()
