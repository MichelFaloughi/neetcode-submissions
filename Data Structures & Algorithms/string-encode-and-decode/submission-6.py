class Solution:

    def encode(self, strs: List[str]) -> str:

        # ["Hello","2World", "hi", "bye"] -
        # "5-Hello6-2World2-hi3-bye"
        #    ^
        res = ""
        for s in strs:
            res += f"{str(len(s))}-{s}" # TODO: do i need str ? 
        return res

    def decode(self, s: str) -> List[str]:
        # "5234-Helwfe...weewflo6-2World2-hi3-bye"
        #      ^
        
        # curr_idx = 0
        # while curr_idx < len(s)
        # get num using delimiter
        #   nxt_length = ""
        #   while s[curr_idx].isdigit()
        #       nxt_length += s[curr_idx]
        #   nxt_length = int(nxt_length)
        #   assert s[nxt_length + 1] == '-'
        # figure out substring, add it to res
        # move curr_idx to next place

        res = []
        curr_idx = 0
        while curr_idx < len(s):
            # compute length of next string
            nxt_str_len = ""
            while s[curr_idx].isdigit():
                nxt_str_len += s[curr_idx]
                curr_idx += 1
            nxt_str_len = int(nxt_str_len)
            assert s[curr_idx] == '-'

            res.append(s[
                curr_idx + 1:curr_idx + 1 + nxt_str_len
                ])
            curr_idx += 1 + nxt_str_len

        return res
