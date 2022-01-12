nums = [2, 7, 11, 15]  # nums = [3, 2, 4]   # nums = [3, 3]
target = 9
result = []

for (index, num) in enumerate(nums):
    tmpList = [nums[index], nums[index + 1]]
    sumNum = sum(tmpList)
    if sumNum == target:
        print(result.append(index))
        print(result.append(index + 1))
    break

print('Input: nums = ' + str(nums) + ', target = ' + str(target))
print('Output:' + str(result))


# 回答
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
