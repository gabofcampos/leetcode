# You are given an array of integers nums and an integer target,
#   return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
#   and you may not use the same element twice.
#
# You can return the answer in any order.
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        parsed = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in parsed:
                return [i, parsed[diff]]
            parsed[num] = i
