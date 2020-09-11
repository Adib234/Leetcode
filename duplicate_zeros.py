class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        store = len(arr)
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 1
                del arr[len(arr)-1]
            i += 1
