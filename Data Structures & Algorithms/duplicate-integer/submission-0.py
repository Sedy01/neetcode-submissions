class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        lst = []
        for i in nums:
            if i in lst:
                return True
            lst.append(i)
        return False