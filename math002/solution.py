



"""
    Calculate the sum of even or odd Fibonacci numbers within a given range.
    Return : The sum of even or odd Fibonacci numbers in the specified range.
"""
def answer():
    """Returns:The sum of even Fibonacci numbers."""
    first, second = 1, 2
    final = 4000000
    total = 0

    while first < final:
        if first % 2 == 0:
            total += first

        first, second = second, first + second

    return total


# def ans(num,target):
#     dict = {}
#     for  i , name  in num :

#         check = target - num 
#         if check in dict :
#             return [check]     



   


def solver(start= 15812, end =91581312, even=False, odd=True):
    """This is a solver function """
    if start > end:
        return 0

    first, second = 0, 1
    even_start, odd_start = 0, 0
    even_end, odd_end = 0, 0

    while first <= start:
        if first % 2 == 0:
            even_start += first
        else:
            odd_start += first

        first, second = second, first + second

    while first <=end:
        if first % 2 == 0:
            even_end += first
        else:
            odd_end += first

        first, second = second, first + second

    if even and not odd:
        final = even_end - even_start
    elif not even and odd:
        final = odd_end - odd_start
    elif even and odd:
        final = even_end - even_start + odd_end - odd_start
    else:
        final = 0

    return final


if __name__ == "__main__":
    print(solver(15812, 91581312, even=False, odd=True))
    print(answer())
  