# Custom sorting we thought of in class
# Create an empty list, find min value in original list
# add to the new list, remove from the old.

nums = [6, 45, 12, 3, 17, 9]
nums_copy = list(nums)

sorted_nums = []

while len(nums_copy) > 0:
    # find min in nums
    minimum = nums_copy[0]
    for value in nums_copy[1:]:
        if value < minimum:
            minimum = value 
    sorted_nums.append(minimum)
    nums_copy.remove(minimum)

print(nums)
print(sorted_nums)