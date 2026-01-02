class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# ✨ Counter:
# - Type of hashmap
# - Count occurrences of each character in both strings and compare.
# - Time complexity: O(n), more efficient for long strings.