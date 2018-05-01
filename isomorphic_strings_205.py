class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        map = {}
        for i in range(0, len(s)):
            if s[i] not in map.keys() and t[i] not in map.values():
               map[s[i]] = t[i]
            elif map.get(s[i]) != t[i]:
                return False
        return True

if __name__ == '__main__':
    solution = Solution
    print(solution.isIsomorphic(solution, 'egg', 'add'))
    print(solution.isIsomorphic(solution, 'foo', 'bar'))
    print(solution.isIsomorphic(solution, 'paper', 'title'))
    print(solution.isIsomorphic(solution, 'ab', 'aa'))