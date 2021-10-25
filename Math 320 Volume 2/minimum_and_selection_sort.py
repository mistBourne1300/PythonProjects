# Exercises 1.13 (i), 1.14 (ii)

# Please don't forget to give the leading order temporal and spatial complexity
# for both implemented functions. You can do so in comments in your code, or in
# your written submission.

# Exercise 1.13 (i)
def argmin(arr):
    """Finds the index of the smallest element of the input list, arr.

    Examples:
        >>> argmin( [1, 2, 3] )
        0
        >>> argmin( [12, 15, 3, 23] )
        2
        >>> argmin( [0, -5, 2, 12] )
        1
    """
    min = arr[0]
    i=1
    while i < len(arr):
        if min > arr[i]:
            min = arr[i]
        i+=1
    return min


# Exercise 1.14 (ii)
def selection_sort(arr):
    """Sorts input arr (of type list) using the "selection sort" algorithm
    described in Exercise 1.14.

    Example:
        >>> selection_sort([2, 4, 1])
        [1, 2, 4]
    """
    i=0
    while i < len(arr):
        next_min = argmin(arr[i:])
        index = arr.index(next_min)
        temp = arr[i]
        arr[i] = next_min
        arr[index] = temp
        i+=1
    return arr


if __name__ == "__main__":
    # You can test your code in this block
    pass
