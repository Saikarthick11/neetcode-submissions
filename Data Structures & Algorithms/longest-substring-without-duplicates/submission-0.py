class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        max_len=0
        seen={}
        for i in range(len(s)):
            c=s[i]
            if c in seen:
                start=max(start,seen[c]+1)
            max_len=max(max_len,i-start+1)
            seen[c]=i
        return max_len
    
        