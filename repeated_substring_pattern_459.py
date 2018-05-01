class repeated_substring_pattern_459(object):
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
        ss = s + s
        ss_trim = ss[1:-1]
        return ss_trim.find(s) != -1

if __name__ == '__main__':
    solution = repeated_substring_pattern_459
    # print(solution.repeatedSubstringPattern(solution, 'abcabc'))
    print(solution.repeatedSubstringPattern(solution, 'abcabc'))