class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count={}
        window_count={}
        if len(s1)>len(s2):
            return False
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        window_size=len(s1)
        for i in range(window_size):
            char=s2[i]
            window_count[char]=window_count.get(char,0)+1
        if s1_count==window_count:
            return True
        for right in range(window_size,len(s2)):
            new_char=s2[right]
            window_count[new_char]=window_count.get(new_char,0)+1
            left=right-window_size
            old_char=s2[left]
            window_count[old_char]-=1
            if window_count[old_char]==0:
                del window_count[old_char]
            if s1_count==window_count:
                return True
        return False      
        