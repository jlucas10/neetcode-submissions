class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        seen = set()
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            
            # Current valid window is [left, right]
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        return max_len