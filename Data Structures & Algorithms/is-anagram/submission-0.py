class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # m1: bruteforce
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else: return False