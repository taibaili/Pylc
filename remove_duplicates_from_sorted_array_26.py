class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in reversed(range(1, len(nums))):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
        return len(nums)

    ## after list pop size will change
    # def remove_duplicates(self, nums):
    #     for i in range(0, len(nums)-2):
    #         if nums[i] == nums[i+1]:
    #             nums.pop(i+1)
    #         i += 1
    #     return len(nums)

if __name__ == '__main__':
    solution = Solution
    # nums1 = [1, 1, 2]
    # ##expected answer is 2
    # print(solution.removeDuplicates(solution,nums1))

    ##expect 5
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    # print(solution.removeDuplicates(solution,nums2))

    print(solution.remove_duplicates(solution, nums2))
