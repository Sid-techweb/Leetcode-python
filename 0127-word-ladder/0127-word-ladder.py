from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, count = q.popleft()

            if word == endWord:
                return count

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new = word[:i] + c + word[i + 1:]

                    if new in words:
                        words.remove(new)
                        q.append((new, count + 1))

        return 0