class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums)-1:
            j += 1
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

solution = Solution()#[0, 1, 2, 3, 4]
result = solution.removeDuplicates([0,0,0,1,1,1,2,2,3,3,4])
print(result)
