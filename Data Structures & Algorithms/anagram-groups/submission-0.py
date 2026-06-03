class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            counts = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                counts[index] += 1
            
            key = tuple(counts)
            if key not in d:
                d[key] = []
            d[key].append(s)
        return list(d.values())