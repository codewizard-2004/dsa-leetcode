from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for item in strs:
            anagrams[tuple(sorted(item))].append(item)

        return list(anagrams.values())