class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mapST = {}
        mapTS = {}
        
        for c1, c2 in zip(s, t):
            # s → t mapping
            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2
            
            # t → s mapping (reverse check)
            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1
        
        return True