class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
            
        lengths = []
        for s in strs:
            lengths.append(len(s))
        return ",".join([str(length) for length in lengths]) + "|" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        delim_i = -1
        for i,c in enumerate(s):
            if c == "|": 
                delim_i = i
                break
        
        coding = s[:delim_i]
        s = s[delim_i+1:]

        codes = [int(code) for code in coding.split(",")]
        result = []
        for i in codes:
            result.append(s[0:i])
            s = s[i:]

        return result