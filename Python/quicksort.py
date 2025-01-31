class Quick_sort:
    def quick_sort(self,nums:list):
        pivot = nums[len(nums) - 1]
        for i in range(0,len(nums) - 1):
            if(nums[i] > pivot):
                for j in range(len(nums) - 1,0,-1):
                    if(nums[j] < pivot):
                        nums[i],nums[j] = nums[j] , nums[i]
                        break
                    if(i>=j):
                        nums[i],pivot = pivot,nums[i]
                        break
        return nums

        '''for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if(nums[i] > nums[len(nums) - 1] and nums[j] < nums[len(nums) - 1]):
                    if(i < j):
                        nums[i] , nums[j] = nums[j] , nums[i]
                    else:
                        nums[i] , nums[len(nums) - 1] = nums[len(nums) - 1] , nums[i]
        return nums'''

obj = Quick_sort()

print(obj.quick_sort([22,11,88,66,55,77,33,44]))