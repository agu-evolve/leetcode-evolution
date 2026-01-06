class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # initialize dic, is key not exist in dic, it create empty list for that key
        ans = defaultdict(list)

        for s in strs:
            
            key = "".join(sorted(s)) # sort alphabetically
            ans[key].append(s) #Group the String

        return list(ans.values())