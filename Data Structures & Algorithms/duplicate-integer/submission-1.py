class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
        lst = []
        size = len(nums)
        for i in nums:
            if i not in lst:
                lst.append(i)
        if len(lst) < size:
            return True
        return False