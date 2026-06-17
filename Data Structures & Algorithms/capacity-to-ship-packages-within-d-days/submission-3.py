class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def greedy(limit):
            curr = 0
            d = 1

            for w in weights:
                if curr + w <= limit:
                    curr += w
                else:
                    d += 1
                    curr = w
                
                if d > days:
                    return -1
            
            return d

        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l + r) // 2
            currDays = greedy(m)

            if currDays == -1:
                l = m + 1
            else:
                r = m - 1
        
        return l