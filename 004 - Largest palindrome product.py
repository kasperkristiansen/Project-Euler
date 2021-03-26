def solve():
    palindromes = []
    for i in range(100,1000):
        for j in range(100,1000):
            if str(i*j) == str(i*j)[::-1]:
                palindromes.append(i*j)
    return max(palindromes)


if __name__ == "__main__":
    print(solve())