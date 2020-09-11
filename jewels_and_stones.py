class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        jewels = set(J)  # search in a set is instant - O(1)
        for stone in S:
            if stone in jewels:
                counter += 1
        return counter
