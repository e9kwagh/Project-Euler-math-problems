"""this is the solver"""
main_dict = {
    1: "one",
    2: "Two",
    3: "Three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "ninteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fivety",
    60: "sixty",
    70: "sevety",
    80: "eigthy",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    100000: "lakh",
    1000000: "million",
    10000000: "crore",
    1000000000: "billion",
}

def answer():
    """this is the ans"""
    return solver(1,1000)

def less_than_100(num):
    """less function"""
    if num == 0:
        return ""
    if num in main_dict:
        return main_dict[num]
    start = num - num % 10
    return main_dict[start] + main_dict[num % 10]


def cal_words(num):
    """cal-words"""
    total = ""
    li = [i for i in main_dict if i <= num]
    i = 1
    divisor = li[-i]
    while divisor >= 100:
        start = num // divisor
        end = num % divisor

        if start in main_dict:
            total += main_dict[start] + main_dict[divisor]
        elif start - (start % 10) in main_dict:
            val_n = start - (start % 10)
            word = main_dict[val_n] + main_dict[start % 10]
            total += word + main_dict[divisor]

        if len(str(end)) <= 2:
            ans = less_than_100(end)
            total += "and" + ans
        i += 1
        divisor = li[-i]
        num = end
    return total


def count_letters_in_words(num):
    """count words"""
    words = cal_words(num)
    return len(words)


def solver(a: int = None, b: int = None):
    """solver"""
    if a is None:
        a = 1
    if b is None:
        a, b = 1, a

    total_letters = 0
    for i in range(a, b + 1):
        total_letters += count_letters_in_words(i)
    return total_letters


if __name__ == "__main__":
    result = solver(1000)
    print(result)
    print(answer())