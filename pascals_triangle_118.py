class pascals_triangle_118:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_number in range(numRows):
            row = [None for _ in range(row_number+1)]
            row[0], row[-1] = 1, 1

            for i in range(1, len(row)-1):
                row[i] = triangle[row_number-1][i-1] + triangle[row_number-1][i]

            triangle.append(row)

        return triangle

if __name__ == '__main__':
    solution = pascals_triangle_118
    print(solution.generate(solution, 1))