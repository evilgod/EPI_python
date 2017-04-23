
class Solution(object):
    def getSum(self,a,b):
        
        sum=a;
        while (b != 0):
             sum=a^b
             b=(a&b)<<1
             a=sum     
        return sum;
    
    def multiply(self,c,d):
        result=0
        while d !=0:
            if d&1:
                result=self.getSum(result,c)
            c=c<<1
            d=d>>1
        return result
        
print Solution().multiply(13, 9)