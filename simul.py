import reinforce
import numpy as np
import math

level = 1
cost = 0

costarray = np.array([])


while costarray.size != 100000:
    result = reinforce.dorein(level)
    price = math.floor(300 * level * (level // 5 + 1) ** (1 + 0.1 * level))

    cost += price

    if result == 1:
        level += 1
    elif result == -5:
        level = 1
    elif result == -10:
        level = 1

    if level == 28:
        costarray = np.append(costarray, cost)
        cost = 0
        level = 1
        # if costarray.size % 1000 == 0:
        #     print(costarray.size)

print(np.percentile(costarray, 10))
print(np.percentile(costarray, 50))
print(np.percentile(costarray, 90))
