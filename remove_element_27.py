class remove_element_27:
    def removeElement(self, nums, val):
        if not nums or len(nums) < 1:
            return 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count = count + 1
        for j in range(count, len(nums)):
            nums[j] = 0
            j = j + 1
        return count

if __name__ == '__main__':
    solution = remove_element_27
    print(solution.removeElement(solution,[3,2,2,3], 3))