def removeDigit(amount, digit):
    maxDigit = ""
    n = len(amount)

    for i in range(n):
        if amount[i] == digit:
            newDigit = amount[:i] + amount[i+1:]
            if newDigit > maxDigit:
                maxDigit = newDigit
    return maxDigit


amount = '1321'
digit = '1'

print(removeDigit(amount, digit))
