s = input()
nums = list(set(s))
counter = dict(zip(nums, nums))

for i in nums:
    counter[i] = s.count(i)

print(*sorted([i for i in counter if counter[i] == max(counter.values())]))