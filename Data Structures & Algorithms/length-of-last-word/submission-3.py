class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        start_index = len(s) - 1
        
        # STEP 1: find start_index of the loop along reversed string
        while s[start_index] == " ":
            start_index -= 1
            if start_index < 0:
                return length

        # STEP 2: loop along reversed string
        for c in s[start_index::-1]:
            if c == " ":
                return length
            else:
                length += 1
        
        return length




        # ' the cat ate the dog '
        # assuming the last character is not a space
        