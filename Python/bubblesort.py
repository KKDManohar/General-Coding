class bubbleSort:
    def bbsort(self,nums:list):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if(nums[j] >= nums[j+1]):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums

bb = bubbleSort()

bb.bbsort([5,3,3,8,6,7,2])