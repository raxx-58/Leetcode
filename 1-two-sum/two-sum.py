class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
            num_map={}    
        # Iterate through the list with index and value
            for i, num in enumerate(nums):
                complement = target - num
            # Check if the complement exists in the map
                if complement in num_map:
                # If found, return the indices
                    return [num_map[complement], i]
            # Add the current number and its index to the map
                num_map[num] = i
        
        # If no solution is found (though problem guarantees one exists)
            return [] 