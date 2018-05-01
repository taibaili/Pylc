class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for e in s:
            if e == '(':
                stack.append(')')
            elif e == '[':
                stack.append(']')
            elif e == '{':
                stack.append('}')
            elif not stack or stack.pop() != e:
                return False
        return not stack


if __name__ == '__main__':
    solution = Solution
    print(solution.isValid(solution, "()"))
    print(solution.isValid(solution, "()[]{}"))
    print(solution.isValid(solution, "(]"))
    print(solution.isValid(solution, "([)]"))
    print(solution.isValid(solution, "{[]}"))