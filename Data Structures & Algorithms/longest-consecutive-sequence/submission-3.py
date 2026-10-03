class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        input array of nums 
        output is length of the longest consecutive seq of elements
        that can be formed. 
        consecutive sequence is if element is exactly 1 greated than the previous element 
        """
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest