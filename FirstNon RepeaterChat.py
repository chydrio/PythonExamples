from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt=Counter(s)
        #help(Counter)
        print(cnt)
        for i in range(len(s)):
            if cnt[s[i]]==1:
                return i
        return -1