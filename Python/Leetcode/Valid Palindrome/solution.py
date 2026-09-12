class Solution:

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move ONLY the left pointer when s[left] is non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            # Move ONLY the right pointer when s[right] is non-alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # Added parentheses () to s[right].lower()
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Ready to run code ==> 
#  :)
# def isPalindrome(s) :
#     left, right = 0, len(s) - 1

#     while left < right:
#            
#         while left < right and not s[left].isalnum():
#             left += 1

#           
#         while left < right and not s[right].isalnum():
#             right -= 1

#         if s[left].lower() != s[right].lower():
#              return False

#          left += 1
#         right -= 1

#     return True