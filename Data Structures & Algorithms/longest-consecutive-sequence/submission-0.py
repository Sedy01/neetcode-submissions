class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = []
        for x in nums:
            if x not in unique_nums:
                unique_nums.append(x)
        disjoint = DisjointSet(unique_nums)

        for x in unique_nums:
            if (x + 1) in disjoint.parent:
                disjoint.union(x, x + 1)
        
        group_counts = {}
        for x in unique_nums:
            root = disjoint.find(x)
            if root not in group_counts:
                group_counts[root] = 0
            group_counts[root] += 1
        
        max_size = 0
        for count in group_counts.values():
            if count > max_size:
                max_size = count
        
        return max_size

class DisjointSet:
    def __init__(self, elements):
        self.parent = {}
        for x in elements:
            self.parent[x] = x
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j