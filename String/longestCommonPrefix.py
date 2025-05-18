def longestCommonPrefix(names):
    n = len(names)
    result = []
    names.sort()

    first = names[0]
    last = names[n-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            break
        result.append(first[i])
    
    return ''.join(result)

names = ["flower","flow","flight"]
print(longestCommonPrefix(names))