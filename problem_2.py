def solve(num):
	x = 1
	y = 2
	sum = 0
	
	while x <= num:
		if x % 2 == 0:
			sum += x
		x, y = y, x + y
	return sum

if __name__ == "__main__":
    print(solve(4000000))
