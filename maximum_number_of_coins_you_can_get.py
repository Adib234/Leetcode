class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        
        start=len(piles)-1
        count=0
        total=0
        piles.sort()
        alternate=False
        while count!=len(piles)//3:
            start-=1
            alternate= not alternate
            if alternate:
                total+=piles[start]
                count+=1
        return total