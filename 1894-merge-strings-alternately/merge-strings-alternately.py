class Solution:
    def mergeAlternately(self, word1: str, word2: str):
        A=[]
        i=max(len(word1),len(word2))
        for j in range(i):
            if j<len(word1):
                A.append(word1[j])
            if j<len(word2):
                A.append(word2[j])
        return "".join(A)

        