class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        indexes = []

        for i in range(n):
            if nums[i] == val:
                indexes.append(i)

        for i in sorted(indexes, reverse=True):
            del nums[i]

        return len(nums)