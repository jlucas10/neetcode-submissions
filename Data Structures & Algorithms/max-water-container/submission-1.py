class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            # right - left is length
            # min - is height of container, go by min due to water cant
            # overfill 
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return result