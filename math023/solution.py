"""
Non-Abundant Sums
"""


def answer():
    """Find the sum ."""

    def get_divisors_sum(num):
        return sum(i for i in range(1, num) if num % i == 0)

    def is_abundant(num):
        return get_divisors_sum(num) > num

    ab_list = [i for i in range(1, 28124) if is_abundant(i)]

    sum_ab = [
        ab_list[i] + ab_list[j]
        for i in range(len(ab_list))
        for j in range(i, len(ab_list))
    ]

    all_num = set(range(1, 28124))
    result = all_num - set(sum_ab)

    return sum(result)


if __name__ == "__main__":
    print(answer())

# 4179871 = ans()
