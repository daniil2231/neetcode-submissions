class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adj = {x: set() for x in wordList}
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                newWord1 = wordList[i][:j] + "#" + wordList[i][j + 1:]

                for k in range(len(wordList)):
                    if i != k:
                        newWord2 = wordList[k][:j] + "#" + wordList[k][j + 1:]

                        if newWord1 == newWord2:
                            adj[wordList[i]].add(wordList[k])
                            adj[wordList[k]].add(wordList[i])
        
        q = deque([[beginWord, 1]])
        seen = set([beginWord])
        while q:
            node, transformations = q.popleft()
            print(node, transformations)

            if node == endWord:
                return transformations

            for neighbor in adj[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append([neighbor, transformations + 1])
        
        return 0