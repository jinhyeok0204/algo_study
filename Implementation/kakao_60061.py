def solution(n, build_frame):
    answer = []

    for line in build_frame:
        x, y, stuff, operate = line

        if operate == 0: # 삭제
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1: # 설치
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])

    answer.sort(key= lambda x: (x[0], x[1], x[2]))
    return answer


def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥인경우
            if y == 0 or [x, y, 1] in answer or [x - 1, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False

        if stuff == 1:
            if [x+1, y-1, 0] in answer or [x, y-1, 0] in answer or ( [x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def main():
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    print(solution(n, build_frame))

main()

