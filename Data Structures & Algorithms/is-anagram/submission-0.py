class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sm = {}
        tm = {}
        for sc in s:
            sm[sc] = sm.get(sc, 0) + 1
        for tc in t:
            tm[tc] = tm.get(tc, 0) + 1
        return sm == tm
        