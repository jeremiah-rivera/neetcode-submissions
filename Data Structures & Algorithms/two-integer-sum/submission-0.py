class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        domain = {}
        for i, val in enumerate(nums):
            difference = target - val
            if difference in domain:
                return [domain[difference], i]
            domain[val] = i
            
