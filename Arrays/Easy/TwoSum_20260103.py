class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type hint (expect to return list containing integer)
        
        # # solution 1 (O(n2) time complexity)
        # checkeds= []

        # # enumerate = loop over a list and get both the index and the value at the same time
        # for i, num in enumerate(nums):
        #     for j, checked in checkeds:
        #         if checked + num == target:
        #             return [j, i]

        #     checkeds.append((i, num))


        # solution 2 O(n)
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            # etc: 9 - 2
            complement = target - nums[i]
            # is there a number 7 somewhere in nums
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # no pair found
        return []


        print(hashmap)

