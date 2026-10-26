class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        l = []
        for i in range(len(words)):
            j = 0
            while (j < len(words)):
                if i != j and words[i] in words[j]:
                    if words[i] not in l:
                        l.append(words[i])
                j += 1
        return l
