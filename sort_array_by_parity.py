class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        index = 0

        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[index], A[i] = A[i], A[index]
                index += 1
        return A
