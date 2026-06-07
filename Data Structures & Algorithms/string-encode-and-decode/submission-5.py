class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i])) + "#" + strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        size = ""
        skip_until = 0

        for i in range(len(s)):
            if i >= skip_until:
                if s[i].isnumeric():
                    size += s[i]
                elif s[i] == "#":
                    length = int(size)

                    start = i + 1
                    end = start + length
                    decoded_strs.append(s[start:end])
                    size = ""
                    skip_until = end
        return decoded_strs
