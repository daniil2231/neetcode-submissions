class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for o in operations:
            if o == "+":
                n1, n2 = stack[-1], stack[-2]
                stack.append(n1 + n2)
            elif o == "C":
                stack.pop()
            elif o == "D":
                n1 = stack[-1]
                stack.append(n1 * 2)
            else:
                stack.append(int(o))

        return sum(stack)