# Given an array nums of n integers, are there elements a, b, c in nums such 
# that a + b + c = 0? Find all unique triplets in the array which gives the 
# sum of zero.
#
# Note: The solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = set()
        p1, p2, p3 = 0, 1, len(nums) - 1
        # print nums
        # print p1, p2, p3
        while (p1 < len(nums)-2):
            i = -nums[p1]
            if (nums[p3] + nums[p3-1]) < i:
                p1 += 1
                p2 += 1
                # print "CONTINUE"
                continue
            while (p2 < p3):
                # print p1, p2, p3
                if (nums[p2] + nums[p3]) < i:
                    p2 += 1
                elif (nums[p2] + nums[p3]) > i:
                    p3 -= 1
                else:
                    ret.add((nums[p1],nums[p2],nums[p3]))
                    p2 += 1
                    p3 -= 1
                    # print ret
            p1 += 1
            p2 = p1 + 1
            p3 = len(nums) - 1
        return list(list(i) for i in ret)
    