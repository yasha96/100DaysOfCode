class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize a pointer to track the position of unique elements
        k = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # update the array by moving the current element to the kth position
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

# Prompt the user to enter the array elements
nums = []
n = int(input("Enter the number of elements: "))
for _ in range(n):
    nums.append(int(input("Enter element: ")))

# Create an instance of the Solution class
solution = Solution()

# Call the removeDuplicates function and print the result
unique_count = solution.removeDuplicates(nums)
print("Number of unique elements:", unique_count)
print("Array after removing duplicates:", nums[:unique_count])

