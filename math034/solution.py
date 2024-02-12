"""
Digit Factorials
"""


def sum_check(num, factorial):
    """sum"""
    return sum(factorial[i] for i in str(num))


def answer():
    """anwser()"""
    factorial = {
        "0": 1,
        "1": 1,
        "2": 2,
        "3": 6,
        "4": 24,
        "5": 120,
        "6": 720,
        "7": 5040,
        "8": 40320,
        "9": 362880,
    }
    product = [num for num in range(10, 100000) if sum_check(num, factorial) == num]
    return sum(product)


if __name__ == "__main__":
    print("question no math034")
    print("answer() =", answer())
