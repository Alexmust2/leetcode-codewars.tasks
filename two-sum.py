from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i in range(len(nums)):
           for j in range(len(nums)):
               if i != j and nums[i] + nums[j] == target:
                   return [i,j]


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))

