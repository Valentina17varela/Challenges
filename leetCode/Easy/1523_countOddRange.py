class Solution:
    def countOdds(self, low, high):
        return (high - low + low % 2 + high % 2) // 2