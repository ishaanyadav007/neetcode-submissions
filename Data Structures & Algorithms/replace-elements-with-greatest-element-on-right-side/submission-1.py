class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # bruetforce m1:
        # for i in range(len(arr)):
        #     maxi=0
        #     if i != len(arr)-1:
        #         for j in range(i+1,len(arr)):
        #             if arr[j] > maxi:
        #                 maxi = arr[j]
        #         arr[i] = maxi
        #     else:
        #         arr[i] = -1
        # return arr

        # preserve arr array. use max() to update maxi
        n=len(arr)
        ans = [0]*n
        for i in range(n):
            maxi=-1
            for j in range(i+1,n):
                maxi = max(maxi,arr[j])
            ans[i]=maxi
        return ans