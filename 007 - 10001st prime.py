from math import sqrt

def is_prime(n):
    if n == 0:
        return False
    elif n == 1:
        return False

    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1

    return True


def solve():
    list_of_primes = []
    for i in range(1,500000):
        if is_prime(i):
            list_of_primes.append(i)

    return list_of_primes[10000]


if __name__ == "__main__":
    print(solve())