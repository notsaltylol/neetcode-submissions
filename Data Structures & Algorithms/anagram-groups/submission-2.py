from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for string in strs:
            anagram = {}
            for s in string:
                anagram[s] = anagram.get(s, 0) + 1
            anagram_key = tuple(sorted(anagram.items()))
            anagram_groups.setdefault(anagram_key, []).append(string)
            
        return list(anagram_groups.values())