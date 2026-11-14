class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        t_counts = {}
        for chara in s:
            s_counts[chara] = s_counts.get(chara, 0) + 1
        for chara in t:
            t_counts[chara] = t_counts.get(chara, 0) + 1
        
        return s_counts == t_counts