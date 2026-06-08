class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # bruetforce m1:
        for i in range(len(arr)):
            maxi=0
            if i != len(arr)-1:
                for j in range(i+1,len(arr)):
                    if arr[j] > maxi:
                        maxi = arr[j]
                arr[i] = maxi
            else:
                arr[i] = -1
        return arr