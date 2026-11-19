# Generate 6 numbers in range 1-49.
# Numbers must be unique.
import random 

nums = []

while len(nums) < 6:
    n = random.randint(1, 49)
    if n not in nums:
        nums.append(n)
    else:
        print(f"duplicate {n}")

sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)