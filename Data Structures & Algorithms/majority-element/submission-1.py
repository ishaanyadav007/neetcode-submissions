class Solution:
    def majorityElement(self, nums: List[int]) -> int:\
        #bruteforce: count no of occurences of each element and #then check condition
        n=len(nums)
        for i in range(n):
            count=0
            for j in range(n):
                if nums[j] == nums[i]:
                    count+=1
                if count > n/2:
                    return nums[i]
        # hash map method:
        # hash={}
        # for i in range(n):
        #     hash[nums[i]] = hash.get(nums[i],0) + 1
        # for key,val in hash.items():
        #     if val > n/2:
        #         return key