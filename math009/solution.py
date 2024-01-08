"""Write code for solver.solver() to find all pythogorean triplets 
whose sum lies between p and q,"""
def answer():
    return solver(1,1000)

def solver(p: int = 1, q: int = 1000):  
    "this is the solver"
    if p is None:
        p = 1
    if q is None:
        p, q = 1, p
    if q < p:
        p, q = q, p

    final = {}

    for a in range(p, q):
        for b in range(a, q - a):
            c = int((a**2 + b**2) ** 0.5)
            total = tuple([a, b, c])
            if a < b < c and p <= sum(total) <= q:
                if sum(total) not in final:
                    final[sum(total)] = [total]
                else:
                    final[sum(total)].append(total)

    return final


if __name__ == "__main__":
    print(solver(12))
    print(answer())