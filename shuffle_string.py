class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        final = []

        for idx, value in enumerate(indices):
            final.append([indices[idx], s[idx]])
        final.sort()
        new_string = ''
        for i in range(len(final)):
            new_string += final[i][1]
        return new_string
    # def restoreString(self, s: str, indices: List[int]) -> str:
    #     res = [''] * len(s)
    #     for index, char in enumerate(s):
    #         res[indices[index]] = char
    #     return "".join(res)
