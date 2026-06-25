class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a >= 0:
                stack.append(a)
            else:
                while stack and -a > stack[-1] and stack[-1] >= 0:
                    stack.pop()
                if stack:
                    if -a == stack[-1]:
                        stack.pop()
                        continue
                    elif -a < stack[-1]:
                        continue
                stack.append(a)

        return stack