class Solution:
    def isValid(self, s: str) -> bool:
        # s is only valid if evert open bracket closes in the correct order
        # meaning ({[]}) versus ([)] 
        stack = []
        #map closing bracket to opening
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for i in s: 
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)
        return True if not stack else False
            
            