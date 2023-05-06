def twoSum(nums,target):
        b=[]
        for i in range(0,len(nums)):
            print (i)
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                  
                    b.append(i)
                    b.append(j)
        return b 
if __name__=="__main__":
    num=[3,2,4]
    target=6
    res=twoSum(num,target)
    print(res)
