class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        curr = ""

        for i in range(1, len(path)):
            if path[i] == "/" and path[i - 1] == "/":
                continue
            
            if path[i] == "/":
                if curr == "..":
                    if res:
                        res.pop()
                elif curr == ".":
                    curr = ""
                    continue
                else:
                    res.append(curr)
                curr = ""
            else:
                curr += path[i]
        
        if curr == ".." and res:
            res.pop()
        elif curr != "" and curr != ".":
            res.append(curr)
        
        return "/" + "/".join(res)
