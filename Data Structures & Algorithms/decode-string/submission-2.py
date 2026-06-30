class Solution:
    def decodeString(self, s: str) -> str:
        # s = 2[a3[b
        # curr = ""
            # pop, s = 2[a3[
            # curr = b
                # pop, s = 2[a3
                # curr = b
                    # pop, s = 2[a
                    # num = 3
                    # curr = b
                        # s = 2[abbb]c
        
        # for c in s:
            # if c is closing bracket:
                # while curr stack elem is not a char:
                    # if last pop == "[" or a number:
                        # add curr elem to number var and pop
                    # else:
                        # add curr elem to curr str we are building and pop and update last pop
                # append number * str
            # else:
                # append c to stack
        
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                build = ""
                while stack and stack[-1] != "[":
                    build = stack.pop() + build
                stack.pop()
                
                n = ""
                while stack and stack[-1].isnumeric():
                    n = stack.pop() + n
                n = int(n)

                stack.append(n * build)
            
        return "".join(stack)