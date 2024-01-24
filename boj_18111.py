from sys import stdin

def main():
    # 인벤토리에 b개의 블록이 있음
    n, m, b = map(int, input().split())

    board = []
    for _ in range(n):
        line = list(map(int, stdin.readline().rstrip().split()))
        board.append(line)

    # time,  0 <= height <= 256 .. 가장 적은 시간 -> 가장 높은 땅높이 구하기
    time, height = 0, 0
    # 블록 제거, 인벤토리에 넣기 2초
    # 블록 꺼내서 블록 넣기 1초

    start = 0
    end = 256

    time = int(1e9)
    while start < end:
        count = 0
        # 이게 땅 높이가 될 것임
        mid = (start + end) // 2

        for line in board:
            for each in line:
                # 더 높으면 빼내야함
                if each > mid:
                    count += 2
                # 더 낮으면 쌓아야함
                elif each < mid:
                    count += 1
                else:
                    continue
        if time < count:
            time = count


