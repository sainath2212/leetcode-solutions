class Solution:
    def minInsertions(self, s: str) -> int:
        open = 0
        insertions = 0
        ind = 0 
        while ind < len(s):
            if s[ind]=="(":
                open+=1 
                ind+=1 
            else:
                if ind+1<len(s) and s[ind+1]==")":
                    ind+=2 
                else:
                    insertions+=1 
                    ind+=1 
                if open>0:open-=1 
                else:insertions+=1 
        return insertions+2*open