from math import sqrt

def smallest_prime_factor(num):
	if num >= 2:
		for i in range(2, int(sqrt(num)) + 1):
			if num % i == 0:
				return i
	return num


def solve():
	num = 600851475143
	while True:
		p = smallest_prime_factor(num)
		if p < num:
			num //= p
		else:
			return num

 
if __name__ == "__main__":
	print(solve())