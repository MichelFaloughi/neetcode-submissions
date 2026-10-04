class Solution:

    def encode(self, strs: List[str]) -> str:

        # ["8Hello","World"]
        # prefix each s by its length
        # -> "632323-8Hell...o5-World"
        #           ^

        return "".join([f"{len(s)}-{s}" for s in strs])

    def decode(self, s: str) -> List[str]:

        res = []
        curr_idx = 0

        while curr_idx < len(s):
            # find the length of the next string using '-'
            nxt_str_len = ""
            while s[curr_idx].isdigit():
                nxt_str_len += s[curr_idx]
                curr_idx += 1
            assert s[curr_idx] == '-'
            nxt_str_len = int(nxt_str_len)

            # add the substring to res
            res.append(s[
                curr_idx + 1: curr_idx + 1 + nxt_str_len
            ])
            # increment curr_idx
            curr_idx += 1 + nxt_str_len

        return res
        
