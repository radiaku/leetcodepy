
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
#     Every adjacent pair of words differs by a single letter.
#     Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#     sk == endWord
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#  
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
#
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#  
#
# Constraints:
#
#     1 <= beginWord.length <= 10
#     endWord.length == beginWord.length
#     1 <= wordList.length <= 5000
#     wordList[i].length == beginWord.length
#     beginWord, endWord, and wordList[i] consist of lowercase English letters.
#     beginWord != endWord
#     All the words in wordList are unique.

from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)]) 
    while queue:
        current_word, steps = queue.popleft()

        if current_word == endWord:
            return steps

        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word) 
                    queue.append((next_word, steps + 1))

    return 0  

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(beginWord, endWord, wordList))
