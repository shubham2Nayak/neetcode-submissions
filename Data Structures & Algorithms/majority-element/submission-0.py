class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        hm = {}

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        for i in hm:
            if hm[i] > n/2:
                return i