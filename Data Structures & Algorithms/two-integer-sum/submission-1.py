class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i in range(len(nums)):
            if nums[i] in complementMap:
                return [complementMap[nums[i]], i]
            complementMap[target - nums[i]] = i