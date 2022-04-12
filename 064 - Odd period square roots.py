def findDistinctWays(n):
    '''
    Find how many different ways one hundred can be written as the sum of at least two positive integers
    
    i.e. 100 = 1 + 99
    '''
    ways = [1] + [0]*n
    for i in range(1, n+1):
        for j in range(i, n+1):
            ways[j] += ways[j-i]
    return ways[n]-1

print(findDistinctWays(100))