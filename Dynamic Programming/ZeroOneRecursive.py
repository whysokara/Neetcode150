# recursion

def zeroOneKnapSack(wt, val, W, n):
    if (n == 0 or W == 0): return 0

    if (wt[n-1] <= W):
        return max(val[n-1] + zeroOneKnapSack(wt, val, W - wt[n-1], n-1), zeroOneKnapSack(wt, val, W, n-1))
    elif (wt[n-1] > W):
        return zeroOneKnapSack(wt, val, W, n-1)


wt = [1,3,4,5]
val = [1,4,5,7]
W = 7
n = len(wt)

print(zeroOneKnapSack(wt, val, W, n))