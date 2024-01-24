def main():
    n, r, c = map(int, input().split())
    size = 2 ** n

    result = z_searching(n, r, c)
    return result

def z_searching(n, row, col):
    result = 0
    while n != 0:
        n -= 1
        size = 2 ** n
        if row < size and col < size:
            result += size * size * 0

        elif row < size and col >= size:
            result += size * size * 1
            col -= size

        elif row >= size and col < size:
            result += size * size * 2
            row -= size

        else:
            result += size * size * 3
            row -= size
            col -= size
    return result


if __name__ == '__main__':
    print(main())







