class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr)):
            arr[i] = arr[i]*2
            if arr.count(arr[i]) > 1:
                return True
            arr[i] = arr[i]//2
        return False
