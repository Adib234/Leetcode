class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(sorted_nums,pivot):
            
            l,r = 0, len(sorted_nums)-1
            while l <= r:
                
                mid=(l+r)//2
            
                if target==sorted_nums[mid]:
                    return (mid + pivot)%len(sorted_nums)
                elif target>sorted_nums[mid]:
                    l,r=mid+1,r
                else:
                    l,r=l,mid-1
            return -1
        
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        
        
        if sorted(nums)!=nums:
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    break
            pivot = i + 1
            sorted_nums = nums[i+1:] + nums[:i+1] 
            return binary_search(sorted_nums,pivot)
        
        else:
            return binary_search(nums,0)
