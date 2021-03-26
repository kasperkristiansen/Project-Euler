"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

def find_pythagorean_triplet():
    for a in range(1,500):
        for b in range(a, 1000):
            c = sqrt(a**2 + b**2)

            if a + b + c == 1000:
                print("a: {}, b: {}, c: {}".format(a,b,c))
                print("sum: {}".format(a+b+c))
                print("product: {}".format(a*b*c))
            

if __name__ == "__main__":
    find_pythagorean_triplet()