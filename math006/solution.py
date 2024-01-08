"""Find the difference between the sum of the squares of the consecutive natural numbers"""
def answer():
    return solver(0,100)

def solver(p=1, q=200):

    """starting with and p and ending at q and the square of the sum of 
    consecutive natural numbers starting with p and q"""
    start = min(p, q)
    end = max(p, q)
    #n = p-q

    sum_each = sum_all = 0

    # sum_all = int(((n*(n+1))/2)**2)

    for i in range(start, end + 1):
        sum_each += i**2
        sum_all += i

    sum_all = sum_all**2
    diff = sum_all - sum_each
    return int(diff)


if __name__ == "__main__":
    print(solver(1, 200))
    print(answer())
