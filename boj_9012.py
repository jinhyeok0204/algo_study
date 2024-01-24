def main():
    t = int(input())
    for _ in range(t):
        ps = input()
        print(solution(ps))


def solution(ps):

    if is_vps(ps):
        return "YES"
    else:
        return "NO"


def is_vps(ps):
    zero_idx = get_idx_of_zero(ps)

    if ps == "":
        return True
    if zero_idx == -1:
        return False

    count = 0
    for i in range(zero_idx+1):
        if ps[i] == "(":
            count += 1
        elif ps[i] == ")":
            count -= 1
            if count == 0:

                if is_vps(ps[zero_idx+1:]):
                    return True
    return False


def get_idx_of_zero(ps):
    count = 0
    for i in range(len(ps)):
        if ps[i] == "(":
            count += 1
        elif ps[i] == ")":
            count -= 1
        if count == 0:
            return i
    return -1


if __name__ == '__main__':
    main()