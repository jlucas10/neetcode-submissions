class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U: input is a list of nums
            output is going to be most frequent elemtns = or < k
        P: add to hashmap for every item, if num is in hasmap coutn+1
        if not in hashmap count set to 1 
            then you would cross check elements with k, and add 
            to a return list whihc is output  
        """
        counts = {}

        for i in nums:
            counts[i] = counts.get(i, 0) + 1

            result = sorted(counts.keys(), key=counts.get, reverse = True)
        
        return result[:k]
            