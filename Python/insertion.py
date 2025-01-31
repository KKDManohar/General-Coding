class insertion_sort:
    def insertion(self,num:list):
        for i in range(1,len(num)):
            j = i
            while(num[j-1] < num[j] and j > 0):
                temp = num[j-1]
                num[j-1] = num[j]
                num[j] = temp

                j = j - 1
        return num


obj = insertion_sort()
print(obj.insertion([2,5,4,5,1]))
