def main():
    n = int(input())
    k = int(input())

    board = [[0] * (n+1) for _ in range(n+1)]
    board[1][1] = 1  # 첫 위치

    for i in range(k):
        ay, ax = map(int, input().split())
        board[ay][ax] = -1  # 사과가 있으면 -1

    l = int(input())
    turn_info = []
    for _ in range(l):
        t, c = input().split()
        turn_info.append((int(t), c))

    time = 0
    y, x = 1, 1
    direction = 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    turn_idx = 0

    body = [(1, 1)]

    while True:
        time += 1

        ny, nx = y + dy[direction], x + dx[direction]

        if ny < 0 or ny >= n or nx < 0 or ny >= n or board[ny][nx] == 1:
            break

        if board[ny][nx] == -1:  # 사과가 있다면
            body.append((ny, nx))
            board[ny][nx] = 1  # 머리의 새로운 위치 넣기
        else:
            ry, rx = body.pop(0)  # 지울 꼬리의 위치
            body.append((ny, nx))
            board[ry][rx] = 0  # 꼬리 지우기
            board[ny][nx] = 1  # 머리의 새로운 위치 넣기

        y, x = ny, nx

        if turn_idx < l and time == turn_info[turn_idx][0]:
            direction = turn(direction, turn_info[turn_idx][1])
            turn_idx += 1

    return time


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


if __name__ == '__main__':
    print(main())
