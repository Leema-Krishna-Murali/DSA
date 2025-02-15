'''Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]'''

class Solution:   
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def BSLR(arr,low,high,searchFlag,target):
            index=-1
            while low<=high:
                mid=(low+high)//2
                if arr[mid]==target:
                    index=mid
                    if searchFlag:
                        high=mid-1
                    else:
                        low=mid+1
                elif arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return index
        BSL = BSLR(nums,0,len(nums)-1,True,target)
        BSR = BSLR(nums,0,len(nums)-1,False,target)
        return [BSL,BSR]



        
        
        