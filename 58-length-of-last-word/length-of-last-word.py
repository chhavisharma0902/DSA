class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        n = len(s)
        count = 0
        if(n==1):
            return 1
        for i in range(n-1,-1,-1):
            if(s[i]==' '):
                break
            else:
                count+=1
        return count
            