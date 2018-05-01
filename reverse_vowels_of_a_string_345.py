
class reverse_vowels_of_a_string_345:
    def reverseVowels(self, s):
        vowel = 'AEIOUaeiou'
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            while s[i] not in vowel and i<j:
                i = i + 1
            while s[j] not in vowel and i<j:
                j = j - 1
            s[i],s[j] = s[j],s[i]
            i, j = i + 1, j - 1
        return ''.join(s)

    def reverse_vowels(self, s):
        vowel = 'AEIOUaeiou'
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            while s[i] not in vowel and i<j:
                i = i + 1
            while s[j] not in vowel and i<j:
                j = j - 1
            s[i],s[j] = s[j],s[i]
            i = i + 1
            j = j - 1
        return ''.join(s)

if __name__=='__main__':
    solution = reverse_vowels_of_a_string_345
    print(solution.reverse_vowels(solution, 'leetcode'))