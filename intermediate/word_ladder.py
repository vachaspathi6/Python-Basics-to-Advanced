from collections import deque, defaultdict

def word_ladder(beginWord, endWord, wordList):
    """
    Finds the shortest transformation sequence from beginWord to endWord such that:
    - Only one letter can be changed at a time.
    - Each transformed word must exist in the wordList.

    Returns:
        A tuple (steps, path) where:
        - steps is the number of words in the shortest transformation sequence.
        - path is a list of words representing the transformation.

    Example:
    >>> word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    (5, ['hit', 'hot', 'dot', 'dog', 'cog'])
    """
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0, []

    # Preprocess: create wildcard patterns (e.g., h*t, ho*)
    neighbors = defaultdict(list)
    for word in wordSet:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            neighbors[pattern].append(word)

    # BFS with path tracking
    queue = deque([(beginWord, [beginWord])])
    visited = set([beginWord])

    while queue:
        word, path = queue.popleft()
        if word == endWord:
            return len(path), path

        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            for nei in neighbors.get(pattern, []):
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, path + [nei]))

    return 0, []


if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    steps, path = word_ladder(begin, end, words)
    if steps:
        print(f"Shortest transformation length: {steps}")
        print("Transformation path:", " → ".join(path))
    else:
        print("No transformation sequence found.")
