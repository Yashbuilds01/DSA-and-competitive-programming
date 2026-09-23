class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        dict2 = {}

        for i in ransomNote:
            dict1[i] = dict1.get(i, 0) + 1

        for i in magazine:
            dict2[i] = dict2.get(i, 0) + 1

        for i in dict1:
            if not (dict1.get(i) <= dict2.get(i, 0)):
                return False

        return True

# Ready to run code ==> 
#  :) 

# def canConstruct( ransomNote magazine) :
#         dict1 = {}
#         dict2 = {}

#         for i in ransomNote:
#             dict1[i] = dict1.get(i, 0) + 1

#         for i in magazine:
#             dict2[i] = dict2.get(i, 0) + 1

#         for i in dict1:
#             if not (dict1.get(i) <= dict2.get(i, 0)):
#                 return False

#         return True