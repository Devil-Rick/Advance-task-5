"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
n = list(map(int, input().split(',')))
res = [[]]
for i in n:
    res += [x + [i] for x in res]
print(res)
