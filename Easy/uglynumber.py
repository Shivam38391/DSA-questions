class Solution:
    def isUgly(self, n: int) -> bool:

        # while (n%2==0): #keep dividing my number by 2 ,if its divisble by 2
        #     n = n//2
        # while (n%3==0):
        #     n = n//3
        # while (n%5==0):
        #     n = n//5
        # if (n==1):
        #     return True
        # else:
        #     return False

        if n <= 0:
            return False
        for i in [2,3,5]:
            while (n%i==0):
                n= n // i 
            
        # return n==1 or--dowm--->
    
        if n==1:
            return True
        else:
            return False