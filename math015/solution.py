"""This is the solver """


def answer():
    """this is the answer()"""
    return solver(20, 20)

def solver(n, m):
    """solver function"""

    flow = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(n + 1):
        flow[i][0] = 1
    for j in range(m + 1):
        flow[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            flow[i][j] = flow[i - 1][j] + flow[i][j - 1]

    return flow[n][m]


if __name__ == "__main__":
    print(solver(4,4))
    print(answer())