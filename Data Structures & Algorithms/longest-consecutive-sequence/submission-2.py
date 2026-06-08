class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr = num
                length = 1

                while curr + 1 in num_set:
                    curr += 1
                    length += 1
            
                if length > longest:
                    longest = length

        return longest

# DSU solution from before works, but a little overkill.
# Implemented DSU to see if it would work and to practice.
# Prev solution was O(n^2) in worst-case after some analysis.
# Optimized O(n) solution using a set.
# Only counts sequences from nums that have no left neighbour.