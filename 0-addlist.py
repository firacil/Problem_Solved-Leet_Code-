class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_list = []
        cur_sum = 0
        if len(nums) <= 1:
            return nums
        else:
            for num in nums:
                cur_sum += num

                sum_list.append(cur_sum)
        
            return sum_list