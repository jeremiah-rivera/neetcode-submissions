class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        characters = {}
        for char in s:
            characters[char] = characters.get(char, 0) + 1

        for char in t:
            characters[char] = characters.get(char, 0) - 1 
        
        for value in characters.values():
            if value != 0:
                return False
        
        return True