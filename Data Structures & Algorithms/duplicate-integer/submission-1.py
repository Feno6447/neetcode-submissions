class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r=[]
        for i in nums:
            if i in r:
                return True
            r.append(i)
        return False