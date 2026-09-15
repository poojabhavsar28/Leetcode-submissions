class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord('a')] += 1
            
            tuple_key = tuple(key)

            if tuple_key not in groups:
                groups[tuple_key] = []
            
            groups[tuple_key].append(word)
        
        return list(groups.values())

