class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hash map method:
        n = len(nums)
        hash={}
        for i in range(n):
            hash[nums[i]] = hash.get(nums[i],0) + 1
        for key,val in hash.items():
            if val > n/2:
                return key