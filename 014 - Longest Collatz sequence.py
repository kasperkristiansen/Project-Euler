"""
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def find_collatz(n):
    collatz_sequence = []
    
    while True:
        collatz_sequence.append(n)
        if n == 1:
            return collatz_sequence
        elif n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1


def longest_collatz(n):
    longest_chain = 0

    for i in range(1, n):
        current_collatz = find_collatz(i)
        if len(current_collatz) > longest_chain:
            longest_chain = len(current_collatz)
            starting_number = i

    return longest_chain, starting_number


if __name__ == "__main__":
    n = 1000000
    ans = longest_collatz(n)
    print(f'Elements in Collatz: {ans[0]}\nStarting number: {ans[1]}')
