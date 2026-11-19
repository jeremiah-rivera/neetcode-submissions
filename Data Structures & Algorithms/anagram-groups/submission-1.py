class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map: { (a_count, b_count, ..., z_count) : ["act", "cat"] }
        anagrams = {}
        
        for s in strs:
            # Fresh 26-letter frequency tally for the current word
            count = [0] * 26
            for char in s:
                # Map 'a'-'z' -> index 0-25 and increment
                count[ord(char) - ord('a')] += 1
            # Freeze list into a tuple so it can act as a dict key
            key = tuple(count)
            anagrams[key] = anagrams.get(key, []) + [s]
        
        return list(anagrams.values())


        