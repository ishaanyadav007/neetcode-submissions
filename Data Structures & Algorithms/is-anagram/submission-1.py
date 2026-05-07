class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # m1: bruteforce: sort both and compare
        return sorted(s) == sorted(t)
        #m2: hash dict
        # hash1={}; hash2={}
        
