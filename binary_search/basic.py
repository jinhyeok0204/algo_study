def binary_search_recursive(nums, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search_recursive(nums, target, start, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, end)


def binary_search(nums, target, start, end):

    while start <= end:

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15]

    target = 14

    print(binary_search(nums,target, 0, len(nums)))
    print(binary_search_recursive(nums, target, 0, len(nums)))


if __name__ == '__main__':
    main()
