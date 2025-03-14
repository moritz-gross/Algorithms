def binary_insertion_sort(arr):
    """
    https://en.wikipedia.org/wiki/Insertion_sort#Variants

    :param arr:
    :return:
    """

    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i

        # Use binary search to find the insertion index for key in arr[0:i]
        while left < right:
            mid = (left + right) // 2
            if key < arr[mid]:
                right = mid
            else:
                left = mid + 1

        # left is now the correct insertion position.
        # Shift the elements to the right to make space for key.
        j = i
        while j > left:
            arr[j] = arr[j - 1]
            j -= 1
        arr[left] = key


if __name__ == "__main__":
    data = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    print("Original array:", data)
    binary_insertion_sort(data)
    print("Sorted array:", data)