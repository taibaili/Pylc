class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        words = str.split(" ")
        if len(pattern) != len(words):
            print(len(pattern))
            return False
        map = {}
        for i in range(0, len(pattern)):
            if pattern[i] not in map.keys() and words[i] not in map.values():
                map[pattern[i]] = words[i]
            elif pattern[i] in map.keys():
                if map[pattern[i]] != words[i]:
                    return False
            elif words[i] in map.values():
                return False
        return True

if __name__ == '__main__':
    solution = Solution
    ##True
    print(solution.wordPattern(solution, 'abba', 'dog cat cat dog'))
    ##False
    print(solution.wordPattern(solution, 'abba', 'dog cat cat fish'))
    ##False
    print(solution.wordPattern(solution, 'aaaa', 'dog cat cat dog'))
    ##False
    print(solution.wordPattern(solution, 'abba', 'dog dog dog dog'))
