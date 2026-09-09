class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# Ready to run code ==>
#     :)
# def containsDuplicate( nums):
#     return len(nums) != len(set(nums))
 