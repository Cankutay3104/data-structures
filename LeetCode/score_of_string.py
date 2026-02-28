# Leetcode '3110. Score of a String' Solution


class Solution:
    def scoreOfString(self, s: str) -> int:
        i, j = 0, 1
        score = 0
        while j < len(s):
            score += abs(ord(s[j]) - ord(s[i]))
            i += 1
            j += 1
        return score