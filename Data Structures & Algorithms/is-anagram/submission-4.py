class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # m1: bruteforce: sort both and compare
        # return sorted(s) == sorted(t)
        #m2: hash dict
        hash1={}; hash2={}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hash1[s[i]] = hash1.get(s[i],0) + 1
            hash2[t[i]] = hash2.get(t[i],0) + 1
        return hash1 == hash2

        # longer version without using get function
        # for i in range(len(s)):
        #     if s[i] in hash1.keys():
        #         hash1[s[i]]+=1
        #     else:
        #         hash1[s[i]]=1

        # for i in range(len(s)):
        #     if t[i] in hash2.keys():
        #         hash2[t[i]]+=1
        #     else:
        #         hash2[t[i]]=1
        # return hash1 == hash2

        #m3: arrays of fixed length, 
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')]+=1
            count[ord(t[i]) - ord('a')]+=1
        for val in count:
            if val != 0:
                return False
        return True

        
