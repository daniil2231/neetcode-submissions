class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        curr = 0

        while l <= r:
            curr += people[r]
            r -= 1
            if curr + people[l] <= limit:
                curr += people[l]
                l += 1
            res += 1
            curr = 0

        return res