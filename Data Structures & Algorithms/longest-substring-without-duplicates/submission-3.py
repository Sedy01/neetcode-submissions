class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            ch = s[right]
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            size = right - left + 1
            if size > longest:
                longest = size

        return longest