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
        
        for i in range(max(weights), 50000 * 500):
            currDays = greedy(i)
            if currDays != -1:
                return i