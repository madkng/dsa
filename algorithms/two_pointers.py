"""
The two pointers algorithm is a technique commonly used in solving problems involving sorted arrays or linked lists.
It involves using two pointers (or indices) to traverse the data structure from different directions,
often starting at the beginning and the end, or at two different positions.

This approach is particularly useful for problems involving searching, sorting, or finding pairs or subarrays
that satisfy a specific condition. By moving the pointers strategically, the algorithm can reduce the time complexity
compared to brute-force solutions.

For example, in the problem of finding the squares of a sorted array, two pointers can be used to compare
the absolute values of the numbers at the start and end of the array, and then place the larger square
at the appropriate position in the result array.


Examples of problems solved by the two pointers technique:

# 1. Finding a pair with a given sum in a sorted array
# 2. Removing duplicates from a sorted array
# 3. Merging two sorted arrays
# 4. Finding the maximum sum of a subarray of size k
# 5. Trapping rainwater problem
# 6. Finding the longest substring without repeating characters
# 7. Partitioning an array into two parts with equal sums
# 8. Finding the closest pair to a target sum in two sorted arrays
# 9. Checking if a string is a palindrome
# 10. Finding the intersection of two sorted arrays
"""

from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    """
    Given a sorted array of integers, this function returns a new array containing
    the squares of each number, also sorted in non-decreasing order.
    The function uses a two-pointer approach to efficiently compute the result
    in O(n) time complexity.
    Args:
      nums (List[int]): A list of integers sorted in non-decreasing order.
    Returns:
      List[int]: A list of the squares of the input integers, sorted in
      non-decreasing order.
    Example:
      >>> sorted_squares([-4, -1, 0, 3, 10])
      [0, 1, 9, 16, 100]
      >>> sorted_squares([-7, -3, 2, 3, 11])
      [4, 9, 9, 49, 121]
    """
    # Time: O(n)
    # Space: O(1)

    left = 0
    right = len(nums) - 1
    result = []

    # Two pointers to create squared array
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left] ** 2)
            left += 1

        else:
            result.append(nums[right] ** 2)
            right -= 1

    # Two pointers to reverse an array
    left = 0
    right = len(nums) - 1

    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return result


def reverse_string(s: List[str]) -> None:
    """
    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.
    """
    left = 0
    right = len(s) - 1

    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1



if __name__ == "__main__":
