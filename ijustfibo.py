# def fibonacci(n1, memo={}):
#     if n1 in memo:
#         return memo[n1]
#     if n1 == 0:
#         return 0
#     if n1 == 1:
#         return 1
#     memo[n1] = fibonacci(n1 - 1, memo) + fibonacci(n1 - 2, memo)
#     return memo[n1]

# def fibonacci2(n1, memo=None):
#     if memo is None:
#         memo = {fibonacci(998), fibonacci(999)}
#     if n1 in memo:
#         return memo[n1]
#     if n1 == 0:
#         return 0
#     if n1 == 1:
#         return 1
#     memo[n1] = fibonacci2(n1 - 1, memo) + fibonacci2(n1 - 2, memo)
#     return memo[n1]

# def main(n):
    

#     return fibonacci2(n)
# print(main(1990))

def fibonacci(n1, memo={}):
    """fibonacci with memoization"""
    if n1 in memo:
        return memo[n1]
    if n1 == 0:
        return 0
    if n1 == 1:
        return 1
    memo[n1] = fibonacci(n1 - 1, memo) + fibonacci(n1 - 2, memo)
    return memo[n1]

def fibonacci2(n1, memo=None):
    """fibonacci with memoization"""
    if memo is None:
        memo = {998: fibonacci(998), 999: fibonacci(999)}
    if n1 in memo:
        return memo[n1]
    if n1 == 0:
        return 0
    if n1 == 1:
        return 1
    memo[n1] = fibonacci2(n1 - 1, memo) + fibonacci2(n1 - 2, memo)
    return memo[n1]

print(fibonacci2(1996))
