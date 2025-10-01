from collections import deque, defaultdict

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    # Preprocess: create patterns like h*t, ho*
    neighbors = defaultdict(list)
    for word in wordSet:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            neighbors[pattern].append(word)

    # BFS
    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps

        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            for nei in neighbors.get(pattern, []):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, steps + 1))

    return 0


if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    words = ["hot","dot","dog","lot","log","cog"]
    print(word_ladder(begin, end, words))  # Output: 5
