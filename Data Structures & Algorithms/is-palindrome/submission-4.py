class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        given string s return T if it is a palindrome
            string that reads forward and backward the same 
            ignore all non alphanumeric character
                use .isalnum() to check if alphanumeric
            return whether it is true and false 
        '''
        left = 0
        right = len(s) - 1

        while left < right: 
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))