class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
        left=0
        right=len(clean)-1
        palindrome=0
        if(clean==""):
            return True
        while left<right:
            if clean[left]==clean[right]:
                left+=1
                right-=1
                palindrome=1
            else:
                return False
        if palindrome==1:
            return True 
        return True
        