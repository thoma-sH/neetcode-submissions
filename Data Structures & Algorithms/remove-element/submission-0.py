class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        last = len(nums) - 1
        while curr <= last:
            if nums[curr]==val:
                nums[curr], nums[last] = nums[last], nums[curr]
                last-=1
            else:
                curr+=1
        return curr