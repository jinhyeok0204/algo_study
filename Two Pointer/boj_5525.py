# slicing 하게 되면 시간복잡도가 O(N^2)이 되어 n이 1000000이 되었을 때 시간초과
# 투 포인터 알고리즘 사용!!

"""
투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현 할 수 있다.

"""
def main():
    n = int(input())
    len_of_s = int(input())
    s = input()

    pn = "IO" * n + "I"
    len_of_pn = len(pn)
    count = 0

    left, right = 0, 0
    while right < len_of_s:
        if s[right:right + 3] == "IOI":
            right += 2
            if right - left + 1 == len_of_pn:
                count += 1
                left += 2
        else:
            right += 1
            left = right

    print(count)

main()