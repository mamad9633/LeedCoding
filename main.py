
'''
Documentation: 

'''
from LeedCoding.leedcode import LeedCode
if __name__ == "__name__":
    leed_obj = LeedCode()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #Pointers initialization
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []
        if len(nums) < 2 :
            print("Enter a list which have more than two elements")
        else:     
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j and nums[i]+nums[j] == target and not i and not j in r:
                        r.append(i)
                        r.append(j)
            return r




class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Les nombres négatifs ne sont pas des palindromes
        if x < 0:
            return False
        
        # Convertir le nombre en chaîne de caractères
        num_str = str(x)
        
        # Comparer la chaîne avec sa version inversée
        return num_str == num_str[::-1]



class Solution:
    def romanToInt(self, s: str) -> int:
        # Romain dictionnary
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prevvalue = 0       
        for char in reversed(s):
            currvalue = values[char]
            
            # If the actual value is less than the previous one
            if currvalue < prevvalue:
                total -= currvalue
            else:
                total += currvalue
            
            prevvalue = currvalue
            
        return total




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0
        if not needle:
            return 0
        
        # If needle is longer than haystack
        if len(needle) > len(haystack):
            return -1
        
        # Run haystack until (len haystack - len needle + 1)
        for i in range(len(haystack) - len(needle) + 1):
            # If substring equal to needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # return -1
        return -1
        