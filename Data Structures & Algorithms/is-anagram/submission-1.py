class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution 1
        # if len(s)!=len(t):
        #     return False
        # return sorted(s)==sorted(t)

        #solution 2
        s_dic={}
        t_dic={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_dic:
                s_dic[s[i]]+=1
            else:
                s_dic[s[i]]=1
        for j in range(len(t)):
            if t[j] in t_dic:
                t_dic[t[j]]+=1
            else:
                t_dic[t[j]]=1
        return s_dic== t_dic
        