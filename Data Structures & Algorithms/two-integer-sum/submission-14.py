class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # m1: bruteforce of 2 loops
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # m2: sorting and two pointer approach
        # A=[]
        # for i,num in enumerate(nums):
        #     A.append([num,i])           # ** REV: This order is imp as sorting is done on the basis of first number in 2D lists
        
        # A.sort() 
        # i, j = 0, len(nums) - 1
        # while i<j:
        #     curr = A[i][0] + A[j][0]
        #     if curr == target:
        #         return [min(A[i][1],A[j][1]),max(A[i][1],A[j][1])]
        #     elif curr > target:
        #         j-=1
        #     else:
        #         i+=1

        #m3: Using hash map two pass
        # my trial an d wrong way
        #hash = {}
        # for i in range(len(nums)):
        #     hash[nums[i]] = i               #** this is wrong for duplicate elements. 
        #     # it will overwrite the next duplicate element
        #     # hence everything
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hash and i != nums[i]: # this is also wrong
        #         return [min(i,hash[diff]),max(i,hash[diff])]
        # 2 pass
        # indices={}
        # for i,n in enumerate(nums):
        #     indices[n] = i
        # for i,n in enumerate(nums):
        #     diff = target - n
        #     if diff in indices and i != indices[diff]:
        #         return [i,indices[diff]]

        # 1 pass:
        indices={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in indices: # and i != indices[diff]:    now this other 
#condition is not needed indices won't have anything pre stored in it
# it will form simultaneously, and hence indices[diff] will never have value already
# as i beforehand
                return [indices[diff],i]
# with dry run, you can check always indicees[diff] will be stored first in indices
# hence uska index will always be smaller than the current i which you stand on in the if condition
            indices[n] = i
# this is done to store nums[i] value and its index as we progress the pass
#there is no point storing indices[diff] as its index is not known at all, fir
# uska mei kya karunga, as indices is hash map for indexes of values

# the only diff between 2 pass and one pass is the indicis hash map is formed simultaneously in one pass code
# and in two pass, it is already formed. so it saves a bit of time and space.



# m2: sorting and two pointer approach
        # A={}
        # for i, num in enumerate(nums):
        #     A[num] = i

        # sums = sorted(nums)
        # i=0
        # e=len(nums)-1
        # while i<e:
        #     if sums[i] + sums[e] == target:
        #         return [min(A[sums[i]],A[sums[e]]),max(A[sums[i]],A[sums[e]])]
        #     elif sums[i] + sums[e] < target:
        #         i+=1
        #     else:
        #         e-=1






