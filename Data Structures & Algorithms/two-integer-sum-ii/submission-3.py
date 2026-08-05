class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Understand: 
            Input = array of integers
            Output = return indices of two number such that 
            they add up to target and index1 < index2(can not be equal)

        Plan and Match: 
            left set to index 0 
            right set to end of array
            while left < right
                sum = left+right
                //1 - based index, so add 1
                if sum == target:
                    return [left + 1, right + 1]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else: 
                right -= 1
        return []
        