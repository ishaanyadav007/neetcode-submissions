class Solution:
    def majorityElement(self, nums: List[int]) -> int:\
        #bruteforce m1: count no of occurences of each element and #then check condition
        n=len(nums)
        # for i in range(n):
        #     count=0
        #     for j in range(n):
        #         if nums[j] == nums[i]:
        #             count+=1
        #         if count > n/2:
        #             return nums[i]
        #neetcode soln for this:
        # for num in nums:
        #     count  = sum(1 for i in nums if i==num)
        #     if count > n/2:
        #         return num

        # hash map method m2:
        # hash={}
        # for i in range(n):
        #     hash[nums[i]] = hash.get(nums[i],0) + 1
        # for key,val in hash.items():
        #     if val > n/2:
        #         return key
        #neetcode hashmap:
        count = defaultdict(int)
        res = maxcnt=0
        for num in nums:
            count[num] += 1
            if count[num] > maxcnt:
                maxcnt = count[num] # this is if version of maxcnt = max(maxcnt, count[num]) but we need num also 
                res = num
        return res











