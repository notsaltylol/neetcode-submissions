class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_index = -1
        for i, n in enumerate(nums):
            if n == 0:
                if zero_index == -1:
                    zero_index = i
                elif zero_index != -1:
                    return [0 for n in nums]
            else: 
                total *= n

        result = []

        if zero_index != -1:
            return [0 for i in range(0,zero_index)] + [total] + [0 for i in range(zero_index+1,len(nums))]

        for n in nums:
            if n == 0:
                result.append(total)
            else:
                result.append(int(total/n))
        return result