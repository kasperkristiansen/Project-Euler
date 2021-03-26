"""
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

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

def sum_of_primes(num):
    prime_list = []
    for i in range(1,num):
        if is_prime(i):
            prime_list.append(i)
    return sum(prime_list)


if __name__ == "__main__":
    print(sum_of_primes(2000000))