## Simple recursion
# def gridTraveller(m,n):
#     if(m==1 and n==1): return 1
#     if(m==0 or n==0): return 0

#     return gridTraveller(m-1,n) + gridTraveller(m, n-1)

# print(gridTraveller(2,3))

## memo

def gridTraveler(m,n, memo={}):
    key = str(m) + ',' + str(n)

    if key in memo: return memo[key]
    if(m==1 and n==1): return 1
    if(m==0 or n==0): return 0

    memo[key] = gridTraveler(m-1,n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]

print(gridTraveler(4,3))