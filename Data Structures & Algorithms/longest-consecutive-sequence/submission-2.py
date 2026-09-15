class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0
        for num in nums:
            currentStreak = 0
            currentNum = num
            if currentNum - 1 not in numSet:
                currentStreak = 1
                while currentNum + 1 in numSet:
                    currentStreak += 1
                    currentNum += 1
            longestStreak = max(currentStreak, longestStreak)
        
        return longestStreak