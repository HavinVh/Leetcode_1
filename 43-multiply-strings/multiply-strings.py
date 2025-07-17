class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1=num1[::-1]
        num2=num2[::-1]
        s1=0
        s2=0
        a=0
        b=0
        #print(num1,num2)
        for i in range(0,len(num1)):
          s1=s1+((10**a))*(int(num1[i]))
          a+=1
        for i in range(0,len(num2)):
          s2=s2+((10**b))*(int(num2[i]))
          b+=1
        
        
            
        answer=s1*s2
        answer=str(answer)
        return answer
        