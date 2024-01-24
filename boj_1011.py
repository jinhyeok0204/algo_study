def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        k = 0

        while y - 1 != x + 1:
            can_go = [k, k-1, k+1]
            

if __name__ == '__main__':
    main()