"""Найти 2 максимальных пары эелментов в массиве"""


import random


def nums_generator(length: int) -> list[list[int]]:
    return [random.randint(0, 20) for i in range(length)]


def max_couple_finder(nums: list[int]) -> list[int]:
    global max_couple
    max_couple = [nums[0], nums[1]]
    for i in range(2, len(nums)-1):
        if nums[i] + nums[i + 1] > sum(max_couple):
            max_couple[0], max_couple[1] = nums[i], nums[i + 1]
    return max_couple


nums = nums_generator(10)
print(nums, max_couple_finder(nums), end=' ')
nums.remove(max_couple[0])
nums.remove(max_couple[1])
print(max_couple_finder(nums))
        
    
    
