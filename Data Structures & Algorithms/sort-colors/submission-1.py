class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = {}
        counter = 0

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        if 0 in hm:
            for i in range(hm[0]):
                nums[i] = 0
                counter += 1
        if 1 in hm:
            for j in range(hm[1]):
                nums[counter] = 1
                counter += 1

        if 2 in hm:
            for k in range(hm[2]):
                nums[counter] = 2
                counter += 1

        