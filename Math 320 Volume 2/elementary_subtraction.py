# Exercise 1.6 (i)


# Since I didn't upload the requirements until after many of you completed the
# assignment, there are no requirements on your function name or return values.
# But don't forget to carefully explain the algorithm in your comments!


# If you haven't completed the coding problem yet, here is a code snippet you
# may use:
def find_larger(minu = [], subt = []):
  for i in range(len(minu)):
    diff = minu[i] - subt[i]
    if diff != 0:
      return diff
  return 0


def subtract(minuend,subtrahend):
    """Subtracts two numbers using the standard elementary school algorithm
    for subtraction of multi-digit integers.

    Inputs:
        x (list[int]) : a list of single-digit integers (the minuend)
        y (list[int]) : a list of single-digit integers (the subtrahend)

    Outputs:
        (list[int]) : a list of single-digit integers representing the
                      difference x - y.

    Example:
        >>> a = [1, 2, 3]
        >>> b = [2, 3]
        >>> subtract(a,b)
        [1, 0, 0]
    """
    # Implement your code here!
    difference = []
    diff = len(minuend) - len(subtrahend)

    if diff > 0:
        print("entered subtrahend insertion")
        for i in range(diff):
            subtrahend.insert(0,0)
    elif diff < 0:
        print("entered minuend insertion")
        diff = -1 * diff
        for i in range(diff):
            minuend.insert(0,0)

    print("minuend:", end="\t")
    print(minuend)
    print("subtrahend:", end="\t")
    print(subtrahend)

    #if the larger of the two numbers is on the bottom, we need to flip them, then multiply the final answer by -1
    diff = find_larger(minuend, subtrahend)
    #print(diff)
    if diff < 0:
        temp_list = minuend
        minuend = subtrahend
        subtrahend = temp_list


    length = len(minuend) - 1
    for i in range(len(minuend)):
        m_digit = minuend[length - i]
        s_digit = subtrahend[length - i]
        if m_digit >= s_digit:
            difference.insert(0,m_digit - s_digit)
        else:
            minuend[length - i - 1] = minuend[length - i - 1] - 1
            difference.insert(0,m_digit + 10 - s_digit)
    if diff < 0:
        difference.insert(0,'-')
    return difference


if __name__ == "__main__":
    # You can run test code in this block
    print(subtract([1,2,3,4,5], [2,3,4,5]))
    pass
