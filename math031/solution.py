"""math031"""


def update_ways(coin, target, comb):
    """update coins"""
    for i in range(coin, target + 1):
        comb[i] += comb[i - coin]


def make_combinations(coins, target):
    """make_combinations"""
    comb = (target + 1) * [0]
    comb[0] = 1

    for coin in coins:
        update_ways(coin, target, comb)

    return comb[target]


def answer():
    """answer()"""
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return make_combinations(coins, 200)


def solver(n):
    """solver()"""
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    return make_combinations(coins, n)


if __name__ == "__main__":
    print("question no 31 :")
    print("solver = ", solver(100))
    print("answer = ", answer())
