import sys

input = sys.stdin.readline

def main():
    n = int(input())
    ary = []
    for i in range(n):
        age, name = input().split()
        ary.append((int(age), name))
    ary.sort(key=lambda x: x[0])

    for each in ary:
        print(*each)
main()
