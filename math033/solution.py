def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def answer():
    pro_num = 1
    pro_deno = 1

    for num in range(10, 100):
        for deno in range(num + 1, 100):
            c_digit = set(str(num)) & set(str(deno))
            if len(c_digit) == 1 and "0" not in c_digit:
                canceled_digit = c_digit.pop()
                cancel_num = int(str(num).replace(canceled_digit, "", 1))
                cancel_deno = int(str(deno).replace(canceled_digit, "", 1))

                if cancel_deno != 0 and num / deno == cancel_num / cancel_deno:
                    pro_num *= cancel_num
                    pro_deno *= cancel_deno

    return pro_deno // gcd(pro_num, pro_deno)


if __name__ == "__main__":
    print("Answer of math033:", answer())
