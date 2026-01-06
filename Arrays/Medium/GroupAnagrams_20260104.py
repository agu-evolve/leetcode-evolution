class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        
        # failed
        for s in strs:
            key = frozenset(s) #frozenset only keeps unique letters and ignores counts.

            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return list(groups.values())