'''Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores). '''

class Solution:
    ## TC - O(2N) ~ O(N)
    ## SC - O(N)
    def removeDuplicates_method1(self, nums: List[int]) -> int:
        n = len(nums)
        dict_nums={}
        for i in range(0,n):
            dict_nums[nums[i]]=0
        print(dict_nums)
        j=0
        for keys in dict_nums:
            nums[j] = keys
            j+=1
        return j

    ## Optimal - TC - O(N), SC - O(1)
    ## 2 pointers

    def removeDuplicates_method2(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        j=i+1
        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1
