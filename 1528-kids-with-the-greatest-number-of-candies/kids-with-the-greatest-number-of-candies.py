class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_num=max(candies)
        #we got the biggest number of canies with that ith kid
        for j in candies: #j is candycount  and we are dealing with list
            if (j + extraCandies) >=max_num:
                result.append(True)
            else:
                result.append(False)
        return result

        
        