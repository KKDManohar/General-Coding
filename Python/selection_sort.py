class Selection_Sort:
    def selectionSort(self,nums:list):
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if(nums[i] > nums[j]):
                    nums[i],nums[j] = nums[j],nums[i]
        
        return nums


obj = Selection_Sort()
print(obj.selectionSort([2,6,5,1,3,4]))