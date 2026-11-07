class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hash_map = {}
        n = len(nums)

        for i in nums:

            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        lst = []

        for i in hash_map:
            if hash_map[i] > (n/3):
                lst.append(i)

        return lst