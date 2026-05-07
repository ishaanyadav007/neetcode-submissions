class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # m1: bruteforce of 2 loops
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return ans

        # m2: sorting and two pointer approach
        # sorted_nums = sorted(nums)
        # i=0
        # e=len(nums)-1
        # while i<e:
        #     if sorted_nums[i] + sorted_nums[e] == target:
        #         return