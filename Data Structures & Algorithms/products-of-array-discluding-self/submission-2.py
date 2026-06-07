class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1
        lst = []
        if not any(nums):
            return nums
        for i in nums:
            if i != 0:
                total = total * i
            else:
                zero_count += 1
        for j in nums:
            if j == 0 and zero_count == 1:
                lst.append(total)
            elif j != 0 and zero_count >= 1:
                lst.append(0)
            elif j == 0 and zero_count > 1:
                lst.append(0)
            else:
                lst.append(total // j)
                
        return lst
