class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
            if s.get(target-num) is not None:
                return [s[target-num], i]
            s[num] = i