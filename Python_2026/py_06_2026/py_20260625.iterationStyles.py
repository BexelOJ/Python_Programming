nums = [1, 2, 3]
print(nums[0])
print(nums[1])
print(nums[2])
print()
print("Lenght of Num: ", len(nums))

# 1.) for-each loop
for x in nums:
    print(x)

print()
# 2.) index-based loop
for i in range(len(nums)):
    print(nums[i])

print()
# 3.) while loop iteration
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

print()
# 4.) iterator-based (advanced)
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print()
