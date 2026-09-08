class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for count in cnt.values():
            if count > 1:
                return True
        return False