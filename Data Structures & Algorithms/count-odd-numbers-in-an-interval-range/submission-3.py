class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def isEven(n: int):
            return n%2==0
        res = (high - low +1 ) //2
        if not isEven(high) and not isEven(low):
            res += 1
        return res
        