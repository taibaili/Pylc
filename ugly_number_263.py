# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
#
# Note:
#
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range.

class ugly_number_263(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        while(num != 0):
            if num == 1:
                return True
            elif num%5 ==0:
                num = num/5
            elif num%3 == 0:
                num = num/3
            elif num%2 == 0:
                num = num/2
            else:
                return False
        return True

if __name__ =='__main__':
    solution = ugly_number_263
    print(ugly_number_263.isUgly(ugly_number_263,0))