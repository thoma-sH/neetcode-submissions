class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        def getmax(start: int) -> int:
            res = max(arr[start+1:], default=-1)
            return res
        
        for i in range(len(arr)):
            arr[i] = getmax(i)
        return arr
