class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ## Iterative solution

        # res = []
        # curr_no = 1

        # for _ in range(n):
        #     res.append(curr_no)

        #     if curr_no * 10 <= n:
        #         curr_no *= 10
        #     else:
        #         while curr_no % 10 == 9 or curr_no >= n:
        #             curr_no //= 10 # remove the last digit
        #         curr_no += 1
        
        # return res

        ## DFS solution
        res = []
        for start in range(1, 10):
            self._generate_lex_no(start, n, res)
        return res

    def _generate_lex_no(self, curr_no: int, limit: int, result: List[int]):

        if curr_no > limit:
            return

        result.append(curr_no)

        for nxt in range(10):
            nxt = curr_no * 10 + nxt

            if nxt <= limit:
                self._generate_lex_no(nxt, limit, result)
            else:
                break
        # 386. Lexicographical Numbers
