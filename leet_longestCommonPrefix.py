def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result=""
        lenth=len(strs[1])
        for i in range(len(strs)):
            if lenth>len(strs[i]):
                lenth=len(strs[i])
        for i in range(lenth):
            count=0
            for j in range(len(strs)):
                if j+1<len(strs):
                    if strs[j][i]==strs[j+1][i] :
                        count=count+1
            if count==len(strs)-1:
                result=result+strs[j][i]
        return result

                         
if __name__=="__main__":
    strs=[]
    n=int(input("enter length array"))
    for i in range(n):
        strs.append(input("enter string elements"))
    res=longestCommonPrefix(strs)
    print(res)
    
