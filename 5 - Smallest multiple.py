def solve(num):
    """
    Reaches maximum recursion depth
    Works when initiated from 232792000, 
    but reaches maximum recursion depth if num < 232792000
    """
    my_list = [x for x in range(1,21)]
    
    if all(num%x == 0 for x in my_list):
        print(num)
    else:
        solve(num+1)


if __name__ == "__main__":
    solve(232792000)