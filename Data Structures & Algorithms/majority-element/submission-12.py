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

        # sorting method m2:
        # sums = sorted(nums)
        # freq=1
        # ans=sums[0]
        # for i in range(1,n):
        #     if sums[i]==sums[i-1]:
        #         freq+=1
        #     else:
        #         freq=1
        #         ans=sums[i]
        #     if freq>n/2:
        #         return ans
        # return ans
        # See m4 after this ** most imp

        # hash map method m3:**
        # hash={}
        # for i in range(n):
        #     hash[nums[i]] = hash.get(nums[i],0) + 1
        # for key,val in hash.items():
        #     if val > n/2:
        #         return key
        #neetcode hashmap:
        # count = defaultdict(int)
        # res = maxcnt=0
        # for num in nums:
        #     count[num] += 1
        #     if count[num] > maxcnt:
        #         maxcnt = count[num] # this is if version of maxcnt = max(maxcnt, count[num]) but we need num also 
        #         res = num
        # return res

        # Boyer-Moore Voting algo m4: ** BEST
        # we don't need to sort, we can just use freq as voting power of that
        # element
        # freq=1; ans=nums[0]
        # for i in range(1,n):
        #     if nums[i]==ans:
        #         freq+=1
        #     else:
        #         freq-=1
        #     if freq==0:
        #         ans=nums[i]
        # return ans

        freq=0; ans=0
        for i in range(n):
            if freq==0:
                ans=nums[i]
            if nums[i]==ans:
                freq+=1
            else:
                freq-=1
            
        return ans
        #Bit manipulation m5:


        
        












