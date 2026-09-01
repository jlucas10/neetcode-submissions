class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        given string s return T if it is a palindrome
            string that reads forward and backward the same 
            ignore all non alphanumeric character
                use .isalnum() to check if alphanumeric
            return whether it is true and false 
        '''
        newStr = ''
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        return newStr == newStr[::-1]
