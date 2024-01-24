def balanced_string(message):
    count = 0
    for idx in range(len(message)):
        if message[idx] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return idx


def alright_string(message):
    count = 0
    for i in message:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def reverse(message):
    reversed_message = ""
    for each in message:
        if each == '(':
            reversed_message += ')'
        else:
            reversed_message += '('
    return reversed_message


def solution(p):
    answer = ""
    if p == '':
        return answer

    idx = balanced_string(p)

    u = p[:idx + 1]
    v = p[idx + 1:]

    if alright_string(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        u = reverse(u)
        answer += u
    return answer


