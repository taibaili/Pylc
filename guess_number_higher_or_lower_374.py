def guess(num):
    target = 6;
    if num > target:
        return 1
    elif num < target:
        return -1
    elif num == target:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = low + (high-low)//2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == 1:
                high = mid -1
            else:
                low = mid + 1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                high = mid - 1
            elif ans == 1:
                low = mid + 1

if __name__ == '__main__':
    solution = Solution
    print(solution.guessNumber(solution, 6))