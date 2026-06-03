import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            d[i] += 1
        return heapq.nlargest(k, d, key=d.get)
        