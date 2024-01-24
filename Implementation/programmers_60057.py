# def solution(s):
#     answer = 1000
#
#     for i in range(1, len(s)+1):
#         # 문자열 나누기
#         ls = []
#         for j in range(0, len(s), i):
#             ls = split_to_substring(s, i)
#
#         shorts = ""
#         if len(ls) == 1:  # 마지막 경우
#             shorts = ls[0]
#         else:
#             # shorts 만드는 곳
#             now = ls[0]
#             count = 0
#             for each in ls:
#                 if each == now:
#                     count += 1
#                 else:
#                     shorts += (str(count) + now)
#                     count = 1
#                     now = each
#             shorts += (str(count) + now)
#
#         length = 0
#         for e in shorts:
#             if e != '1':
#                 length += 1
#
#         answer = min(answer, length)
#
#     return answer
#
#
# def split_to_substring(s, n):
#     substrings = []
#     for i in range(0, len(s), n):
#         substrings.append(s[i:i+n])
#     return substrings

def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        shorts = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                shorts += str(count) + prev if count >=2 else prev
                prev = s[j:j+step]
                count = 1

            shorts += str(count) + prev if count >= 2 else prev
            answer = min(answer, len(shorts))
def main():
    s = input()
    print(solution(s))


if __name__ == '__main__':
    main()
