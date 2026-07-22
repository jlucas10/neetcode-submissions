class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            #only store sorted words so same one at the sorted location
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())