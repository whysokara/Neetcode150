## Fib

# def fib(n):
#     if(n<=2):
#         return 1;
#     else:
#         return fib(n-1) + fib(n-2)
    
# print(fib(7))

## 2^n time
## Breaking larger problem into smaller problems is DP

## Memoization
## Python hasmap/dict
def fib(n, memo={}):
    if n <= 2: return 1
    if n in memo: return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(7))  # Output: 13