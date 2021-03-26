def solve():
    counter = 0

    for i in range(3,1000):
        if i % 3 == 0 or i % 5 == 0:
            counter += i
    return counter

if __name__ == "__main__":
    print(solve())