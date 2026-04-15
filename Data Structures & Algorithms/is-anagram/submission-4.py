class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)
        # seems better than his solutions
        
# learnings: 
# - look at his solution, much more simpler and elegant
# - my old solution:
# s_freq_dict = {}
        # t_freq_dict = {}

        # for letter in s:
        #     if letter in s_freq_dict:
        #         s_freq_dict[letter] += 1
        #     else:
        #         s_freq_dict[letter] = 1
        
        # for letter in t:
        #     if letter in t_freq_dict:
        #         t_freq_dict[letter] += 1
        #     else:
        #         t_freq_dict[letter] = 1 
        
        # return s_freq_dict == t_freq_dict