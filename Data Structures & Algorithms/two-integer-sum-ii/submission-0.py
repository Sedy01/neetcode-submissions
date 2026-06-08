class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in numbers and num != numbers[i]:
                return [i + 1, numbers.index(num) + 1]
