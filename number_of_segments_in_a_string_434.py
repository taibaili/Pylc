class number_of_segments_in_a_string_434:
    def countSegments(self, s):
        count = 0
        for i in range(len(s)):
            if(i==0 or s[i-1] is ' ') and (s[i] != ' '):
                count += 1
        return count

    def count_segments_python(self, s):
        return len(s.split())

if __name__ == '__main__':
    solution = number_of_segments_in_a_string_434
    print(solution.countSegments(solution, 'Hello, my name is John'))
    print(solution.countSegments(solution, "love live! mu'sic forever"))
    # print(solution.count_segments_python(solution, "love live! mu'sic forever"))
    # print(solution.count_segments_python(solution, 'Hello, my name is John'))