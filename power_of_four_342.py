class power_of_four_342:
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        remaining = 0
        while num > 1:
            remaining = num % 4
            num = num / 4
        if int(remaining) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = power_of_four_342
    print('is 16 power of four: ' + str(solution.isPowerOfFour(solution, 16)))
    # print('is 8 power of four: ' + str(solution.isPowerOfFour(solution, -2147483648)))