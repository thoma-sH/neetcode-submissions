class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        largest = 0
        for num in nums:
            if num == 1:
                counter+=1
                if largest < counter:
                    largest = counter
            elif num != 1:
                counter = 0
        return largest