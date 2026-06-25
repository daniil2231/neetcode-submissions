class StockSpanner:

    def __init__(self):
        self.l = []

    def next(self, price: int) -> int:
        res = 1

        for i in range(len(self.l) - 1, -1, -1):
            if price < self.l[i]:
                break
            res += 1
        self.l.append(price)

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)