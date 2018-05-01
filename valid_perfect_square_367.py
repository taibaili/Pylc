class valid_perfect_square_367:

    ##brute force will have time limit exceed error
    def isPerfectSquare_2(self, num):
        if num is 1:
            return True
        i = 1
        while i <= num/2:
            if i*i == num:
                return True
            i = i + 1
        return False

    ##time complexity is sqrt n
    def isPerfectSquare(self, num):
        if num is 1:
            return True
        i , res = 1, 0
        while num>0:
            num = num - i
            i = i + 2
        if num == 0:
            return True
        return False

    ##think about binary search solution O(logn)


if __name__ == '__main__':
    solution = valid_perfect_square_367
    # print(solution.isPerfectSquare(solution, 2147483647))
    print(solution.isPerfectSquare(solution, 14))