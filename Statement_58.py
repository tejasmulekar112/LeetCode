class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading and trailing spaces
        s = s.strip()
        
        # Split by spaces
        words = s.split()
        
        # Length of the last word
        return len(words[-1])