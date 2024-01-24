def main():
    m, n = map(int, input().split())

    d_out_value = [[0] * (n+1)]  # 여기에 가중치 값 더해지기
    d_save_value = [[0] * (n+1) for _ in range(m+1)] # 저장 값 저장하기 가중치 더하지 않기

    for i in range(m):
        d_line = list(map(int, list(input())))
        d_line.insert(0, 0)
        d_out_value.append(d_line)

    print(d_out_value)
    for j in range(1, n+1):
        for i in range(1, m+1):
            inputs = make_inputs(d_out_value, i, j)
            save_value = max(inputs)
            d_save_value[i][j] = save_value
            d_out_value[i][j] += save_value


    result = 0
    for line in d_save_value:
        if result < max(line):
            result = max(line)
    print(result)


def make_inputs(d_out_value, i, j) -> list[int]:
    inputs = []
    for a in range(i):
        for b in range(j):
            if b < j and abs(i-a) <= j-b:
                inputs.append(d_out_value[a][b])
    return inputs


if __name__ == '__main__':
    main()