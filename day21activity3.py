nums = [4, 5, 8, 7, 9, 2, 2, 2, 3, 1, 4, 6, 5]
sum = 0

print(nums)

for a in nums:
    sum += a

nums.sort()
mean = round(sum / len(nums), 2)

first = nums[0]
last = nums[-1]

print(f"Sum: {sum}")
print(f"Mean: {mean}")
print(f"Smallest: {first}")
print(f"Greatest: {last}")