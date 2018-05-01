# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class NumberOfOneBits(object):
    def hammingWeight(self, n):
        i = 0;
        while(n != 0):
            x = n & 1
            n = n >> 1
            if x == 1:
              i = i + 1
        return i

if __name__ =='__main__':
    solution = NumberOfOneBits
    print(solution.hammingWeight(solution,13))
