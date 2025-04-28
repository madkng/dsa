"""
The sliding window technique is a commonly used algorithmic approach for solving problems that involve arrays, lists, or strings.
It is particularly useful for problems that require finding subarrays or substrings that satisfy certain conditions, such as:

1. Finding the maximum or minimum sum of a subarray of fixed size.
2. Counting the number of substrings that meet specific criteria.
3. Solving problems related to contiguous subarrays or substrings.

The idea is to use a "window" that slides over the data structure, maintaining a subset of elements at any given time.
This approach helps reduce the time complexity of brute-force solutions by avoiding redundant computations.

There are two main types of sliding window techniques:

1. **Fixed-size Sliding Window**:
  - In this approach, the window size remains constant throughout the process.
  - It is typically used for problems where you need to process subarrays or substrings of a fixed length.
  - Example: Finding the maximum sum of a subarray of size `k`.

2. **Dynamic-size Sliding Window**:
  - In this approach, the window size can grow or shrink dynamically based on the problem's constraints.
  - It is used for problems where the window size depends on certain conditions being met.
  - Example: Finding the smallest subarray with a sum greater than or equal to a target value.

The key difference between the two is that the fixed-size sliding window has a constant size, while the dynamic-size sliding window adjusts its size based on the problem's requirements.
"""

# Example problem
"""
Given a string s, find the length of the longest substring without repeating characters
"""
from typing import List


def lengthOfLongestSubstring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters using a dynamic sliding window technique.
    This function employs the sliding window approach, specifically a dynamic or adjustable sliding window,
    to efficiently determine the maximum length of a substring in the given string `s` that contains only unique characters.
    The window dynamically adjusts its size by expanding to include new characters and contracting when duplicate characters are encountered.
    Sliding Window Type:
      Dynamic Sliding Window - The window size is adjusted dynamically by moving the left pointer forward
      whenever a duplicate character is encountered, ensuring that the substring within the window always
      contains unique characters.

    Args:
      s (str): The input string to analyze.
    Returns:
      int: The length of the longest substring without repeating characters.
    Example:
      >>> lengthOfLongestSubstring("abcabcbb")
      3
      >>> lengthOfLongestSubstring("bbbbb")
      1
      >>> lengthOfLongestSubstring("pwwkew")
      3
    """
    unique_chars = set()
    longest = 0

    left = right = 0

    for right in range(len(s)):
        while s[right] in unique_chars:
            unique_chars.remove(s[left])
            left += 1

        current_window = (right - left) + 1
        longest = max(longest, current_window)
        unique_chars.add(s[right])

    return longest


def findMaxAverage(nums: List[int], k: int) -> float:
    """
    Finds the maximum average of any contiguous subarray of length `k` in the given list of integers using the fixed-size sliding window technique.
    The sliding window technique is employed to efficiently calculate the sum of the subarray of length `k` as the window moves through the array. This avoids recalculating the sum from scratch for overlapping subarrays, reducing the time complexity.
    Sliding Window Type:
      Fixed-size Sliding Window - The window size remains constant at `k` throughout the process.

    Args:
      nums (List[int]): A list of integers.
      k (int): The length of the subarray for which the maximum average is to be calculated.
    Returns:
      float: The maximum average of any contiguous subarray of length `k`.
    Raises:
      ValueError: If `k` is greater than the length of `nums` or if `k` is less than or equal to 0.
    Example:
      >>> findMaxAverage([1, 12, -5, -6, 50, 3], 4)
      12.75
    """
    if k > len(nums) or k <= 0:
        raise ValueError("Invalid value of k")

    curr_sum = sum(nums[:k])
    max_avrg = curr_sum / k

    for i in range(k, len(nums)):
        curr_sum += nums[i]
        curr_sum -= nums[i - k]
        avrg = curr_sum / k
        max_avrg = max(max_avrg, avrg)

    return max_avrg


if __name__ == "__main__":
    print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
