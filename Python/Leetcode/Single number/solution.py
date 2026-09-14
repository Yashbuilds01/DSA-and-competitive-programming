class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique=0
        for i in nums:
            unique^=i
        return unique


# Ready to run code ==> 
#  :) 
# def singleNumber(nums):
#         unique=0
#         for i in nums:
#             unique^=i
#         return unique
