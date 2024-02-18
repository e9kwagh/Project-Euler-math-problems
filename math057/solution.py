"math057"


# def answer(num, deno, limit, count=0):
#     """
#     recurresion
#     """
#     if limit == 0:
#         return count

#     next_num = num + 2 * deno
#     next_deno = num + deno

#     if len(str(next_num)) > len(str(next_deno)):
#         count += 1
#     return answer(next_num, next_deno, limit - 1, count)


def answer(num, deno, limit):
    """plane"""
    count = 0

    for _ in range(limit):
        next_num = num + 2 * deno
        next_deno = num + deno

        if len(str(next_num)) > len(str(next_deno)):
            count += 1
        num, deno = next_num, next_deno

    return count


if __name__ == "__main__":
    print("Answer of math057 =", answer(3, 2, 1000))
