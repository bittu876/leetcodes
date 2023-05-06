def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        result=False
        revers=0
        if x<0:
            return result
        else:
            while temp > 0:
                revers=revers*10+temp%10;
                temp=temp//10
                print(temp)
            print(revers)
            if revers == x:
                result=True
            return result


if __name__=="__main__":
    num=int(input("enter a number"))
    res=isPalindrome(num)
    print(res)
