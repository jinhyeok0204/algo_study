# 응시자 A
# 총감독관 감시 -> B only 1
# 부감독관 감시 -> C 여러명


n = int(input())

room = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for each_room in room:
    each_room -= b
    result += 1

    while each_room > c:
        p = each_room // c
        each_room = each_room % c
        result += p
    if each_room > 0:
        result += 1

print(result)
