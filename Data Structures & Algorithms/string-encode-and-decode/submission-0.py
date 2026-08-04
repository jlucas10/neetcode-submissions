class Solution:
    """
    U - 
        input: lists of strings 
        output: single string 
        Decode is the oposite, 
        single string back to a list of string

        Need to create a delimiter, be bale to know when one word
        ends and another begins
    P - encode:
            store strings encoded into result seperated by delimiter
        decode: 
            take result and loop through s, if delimter seen split word 
            then continue through next word + 1 after delim
            append to res and move i forward 

    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "-" + s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "-":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

