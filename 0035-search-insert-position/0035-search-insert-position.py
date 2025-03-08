class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                index = i
                break
            elif nums[i] < target:
                index = i + 1
                i += 1
        return index
        