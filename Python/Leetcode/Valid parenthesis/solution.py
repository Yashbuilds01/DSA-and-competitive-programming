class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in set("({["):
                lst.append(i)
            elif i in set(")}]"):
                # Check if list is empty BEFORE popping
                if not lst or mapping[i] != lst.pop():
                    return False

        # Returns True if list is empty, False if items remain
        return len(lst) == 0

# Ready to run code ==> 
#  :)
# def isValid(self, s: str) -> bool:
#     lst = []
#     mapping = {")": "(", "]": "[", "}": "{"}

#     for i in s:
#         if i in set("({["):
#             lst.append(i)
#         elif i in set(")}]"):
#          # Check if list is empty BEFORE popping
#             if not lst or mapping[i] != lst.pop():
#                 return False

#         # Returns True if list is empty, False if items remain
#     return len(lst) == 0