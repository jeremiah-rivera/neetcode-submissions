class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for chara in s:
            counts[chara] = counts.get(chara, 0) + 1
        
        for chara in t:
            counts[chara] = counts.get(chara, 0) - 1
        
        for count in counts.values():
            if count != 0:
                return False
        return True
        
        