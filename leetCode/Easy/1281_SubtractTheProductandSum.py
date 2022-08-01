class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        self.list = list(map(int,list(str(n))))
        self.product = 1
        self.sum = 0
        
        for i in self.list:
            self.product *= i
            self.sum += i
            
        return self.product - self.sum