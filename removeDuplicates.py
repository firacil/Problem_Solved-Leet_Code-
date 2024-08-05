"""
    Leet code easy array problem to remove duplicated element in array
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if nums > 0:
            while i < len(nums):
                if nums[i] >= (-100) and nums[i] <= (100):
                    if i + 1 < len(nums):
                        if nums[i] == nums[i + 1]:
                            del nums[i + 1]
                        else:
                            i += 1
                    else:
                        return
                else:
                    return
        print(nums)