import sys


def main():
    n = int(input())
    things = list(map(int, sys.stdin.readline().rstrip().split()))

    things.sort()

    m = int(input())
    to_find = list(map(int, sys.stdin.readline().rstrip().split()))

    for each in to_find:
        if binary_search(things, each, 0, len(things)) != -1:
            print("yes", end =" ")
        else:
            print("no", end = " ")


def binary_search(things, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if things[mid] == target:
            return mid
        elif things[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


main()
