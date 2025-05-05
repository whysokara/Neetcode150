def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()

        x = stones.pop()
        y = stones.pop()

        if x != y:
            stones.append(x - y)

    return stones[0] if stones else 0

stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))