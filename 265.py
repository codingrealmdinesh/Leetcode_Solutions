from functools import lru_cache
import math

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        # Start by defining n and k to make the following code cleaner.
        n = len(costs)
        if n == 0: return 0 # No houses is a valid test case!
        k = len(costs[0])

        # If you're not familiar with lru_cache, look it up in the docs as it's
        # essential to know about.
        @lru_cache(maxsize=None)
        def memo_solve(house_num, color):

            # Base case.
            if house_num == n - 1:
                return costs[house_num][color]

            # Recursive case.
            cost = math.inf
            for next_color in range(k):
                if next_color == color:
                    continue # Can't paint adjacent houses the same color!
                cost = min(cost, memo_solve(house_num + 1, next_color))
            return costs[house_num][color] + cost

        # Consider all options for painting house 0 and find the minimum.
        cost = math.inf
        for color in range(k):
            cost = min(cost, memo_solve(0, color))
        return cost
###
def minCostII(self, costs: List[List[int]]) -> int:
    n = len(costs)
    if n == 0: return 0 # This is a valid case.
    k = len(costs[0])

    # Firstly, we need to determine the 2 lowest costs of
    # the first row. We also need to remember the color of
    # the lowest.
    prev_min_cost = prev_second_min_cost = prev_min_color = None
    for color, cost in enumerate(costs[0]):
        if prev_min_cost is None or cost < prev_min_cost:
            prev_second_min_cost = prev_min_cost
            prev_min_color = color
            prev_min_cost = cost
        elif prev_second_min_cost is None or cost < prev_second_min_cost:
            prev_second_min_cost = cost

    # And now, we need to work our way down, keeping track of the minimums.
    for house in range(1, n):
        min_cost = second_min_cost = min_color = None
        for color in range(k):
            # Determime cost for this cell (without writing it into input array.)
            cost = costs[house][color]
            if color == prev_min_color:
                cost += prev_second_min_cost
            else:
                cost += prev_min_cost
            # And work out whether or not it is a current minimum.
            if min_cost is None or cost < min_cost:
                second_min_cost = min_cost
                min_color = color
                min_cost = cost
            elif second_min_cost is None or cost < second_min_cost:
                second_min_cost = cost
        # Transfer currents to be prevs.
        prev_min_cost = min_cost
        prev_min_color = min_color
        prev_second_min_cost = second_min_cost

    return prev_min_cost