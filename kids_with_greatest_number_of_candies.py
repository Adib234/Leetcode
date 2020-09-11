class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        statement = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                statement.append(True)
            else:
                statement.append(False)
        return statement
