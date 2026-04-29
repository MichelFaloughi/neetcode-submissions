from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def is_valid(freq:dict, k:int) -> bool: # assume freq never empty

            if not freq:
                return True
            maxVal = max(freq.values())          # correct max
            total = sum(freq.values()) - maxVal  # replacements needed
            return total <= k

        l, r = 0, 0
        freq = defaultdict(int)
        freq[s[0]] = 1
        res = 1

        while r < len(s): # TODO: maybe add cond l < r
            currS = s[l:r+1] # check if r+1 or something, watch obo

            # for a, b in freq.items():
            #     print('key: ', a)
            #     print('val: ', b)
            # print('')

            if is_valid(freq, k):
                res = max(res, len(currS))
                r += 1
                if r < len(s):
                    freq[s[r]] += 1
            
            else:
                freq[s[l]] -= 1
                l += 1 

        return res



        

                

        # " A A A B A B B ", k=1
        #   l
        #       r  

        # init l,r = 0,0
        # freq = {}
        # while r < len(s)          keep r in bounds, TODO: maybe add l while l<r
        # get currS = s[l:r] or r+1
        # 
        #
        #
        # check if valid
        #   if valid: res = max(res, currS, key=len), THEN increment r, update dict, watch obo
        #   else:  update dict, THEN increment l
        # return res

        # from collections import defaultdict
        # freq = {}
        # check if dict is valied (pop max, add rest, <k)      









        # def is_valid(s:str, k:int) -> bool:
        #     ''' checks if s has at MOST k 'mistakes' '''
        #     # make a frequency dict for all c in s
        #     # pop the character with most freq
        #     # add all the other frequencies up, if greater than k false, else true
        #     pass

        # majL, num_majL, diffL = s[0], 1, 0 # majority letter and num different letters


  
       
