def turn_a_matrix_90_degree(a : list):
    n = len(a) # 아래 길이 ( 행)
    m = len(a[0]) # 옆 길이 ( 열)
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result