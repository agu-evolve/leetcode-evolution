class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        checked = set()
        
        # use set instead of list to prevent O(n²)
        for num in nums:
            # o(k) for list 
            if num in checked:
                return True
            checked.add(num)
        
        return False
        

# ✨ SET
# - Unordered
# - Unique elements only
# - Fast membership checking
#     - Is 5 already in the set? —> 5 in my_set
#     - For a list, Python has to look at each element one by one → O(n)
#     - For a set, Python can do it almost instantly → O(1) on average
# - Mutable (add or remove)