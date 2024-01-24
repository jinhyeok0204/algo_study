def main():
    n, m = map(int ,input().split())
    now_y, now_x, d = map(int, input().split())
    room = []
    for i in range(n):
        room.append(list(map(int, input().split())))

    # 북, 동, 남, 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    count = 0
    while True:

        if room[now_y][now_x] == 0:
            room[now_y][now_x] = -1
            count += 1
        # 4방면의 방이 청소되었는지 확인
        all_clean = True
        for i in range(4):
            ny, nx = now_y + dy[i], now_x + dx[i]
            # 벽이 아니고 청소가 안 되어 있다면
            if not out_range(nx, ny, n, m) and room[ny][nx] == 0:
                all_clean = False
                break

        # 모두 깨끗함
        if all_clean:
            # 방향을 유지한 채로 한 칸 후진
            ny, nx = now_y - dy[d], now_x - dx[d]
            # 뒤쪽 칸이 벽이라면 작동 멈추기
            if out_range(nx, ny, n, m) or room[ny][nx] == 1:
                break
            else:
                now_y, now_x = ny, nx
                continue

        # 모두 깨끗하지 않음
        elif not all_clean:
            for i in range(4):
                # 반시계 방향 90도 회전
                d = (d - 1) % 4
                # 한칸 전진했을 때 위치
                ny, nx = now_y + dy[d], now_x + dx[d]
                # if 겅계에 닿지 않고 and 청소 x
                if not out_range(nx, ny, n, m) and room[ny][nx] == 0:
                    now_y, now_x = ny, nx
                    break
                else:
                    continue
    print(count)


def out_range(nx, ny, n, m):
    return nx < 0 or nx >= m or ny < 0 or ny >= n


if __name__ == '__main__':
    main()

