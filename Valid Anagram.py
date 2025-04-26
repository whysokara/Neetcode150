# ## Brute Force
s = "anagram"
t = "nagaam"

# if len(s) != len(t):
#     print(False)

# countS, countT = {}, {}

# for i in range(len(s)):
#     countS[s[i]] = 1 + countS.get(s[i],0)
#     countT[t[i]] = 1 + countT.get(t[i],0)

# for c in countS:
#     if countS[c] != countT.get(c,0):
#         print(False)
# print(True)

## Solution 2

# count = {}

# for x in s:
#     count[x] += 1

# for x in t:
#     count[x] -= 1

# for val in count.values():
#     if val != 0:
#         print(False)

# print(True)
if sorted(s) != sorted(t):
    print(False)