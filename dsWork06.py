from itertools import permutations

def main():
    ls = list(range(1, 10))
    p = list(permutations(ls, 3))
    print(p)



main()
