class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(l, num):
            if len(l) == k:
                res.append(l.copy())
                return
            
            for i in range(num, n + 1):
                l.append(i)
                backtrack(l, i + 1)
                l.pop()
        
        backtrack([], 1)
        return res