class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        U- 
            input = array of heights where heights[i] represnt height
            of i bar
            ouput = max amount fo water a container can store (max())
            assumptions = calculation for getting amount of water 
            container can hold (area)
        P-
            set left, right = 0, len(heights) - 1
            result = 0
            while left < right
                calculate area 
                compare recent result to new area calculation
                if left of container is <= right left goes up 1
                else if right is < left right goes down one 
            return result
        """
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            if area > result:
                result = area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return result