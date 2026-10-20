class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.setdefault(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, frequency in frequencies.items():
            buckets[frequency].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result