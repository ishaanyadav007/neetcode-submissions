class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # m1: bruteforce of 2 loops
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # m2: sorting and two pointer approach
        A=[]
        for i,num in enumerate(nums):
            A.append([num,i])           # ** REV: This order is imp as sorting is done on the basis of first number in 2D lists
        
        A.sort() 
        i, j = 0, len(nums) - 1
        while i<j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [min(A[i][1],A[j][1]),max(A[i][1],A[j][1])]
            elif curr > target:
                j-=1
            else:
                i+=1








