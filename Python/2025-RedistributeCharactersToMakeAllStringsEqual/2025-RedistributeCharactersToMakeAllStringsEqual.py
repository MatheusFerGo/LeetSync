# Last updated: 25/09/2025, 08:27:12
class Solution:
    def makeEqual(self, words):
        n = len(words)
        freq = [0] * 26

        for word in words:
            for c in word:
                freq[ord(c) - ord('a')] += 1
        
        for count in freq:
            if count % n != 0:
                return False
        return True