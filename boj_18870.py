def main():
    n = int(input())
    nums = list(map(int, input().split()))

    sorted_nums = sorted(list(set(nums)))
    d = dict(zip(sorted_nums, list(range(len(sorted_nums)))))

    for x in nums:
        print(d[x], end=" ")



if __name__ == '__main__':
    main()