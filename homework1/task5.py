from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if k > len(nums) or len(nums) == 0 or k == 0:
        raise ValueError("Invalid input")
    max_sum = 0
    while k > 0:
        for i in range(len(nums) - k + 1):
            if sum(nums[i: i + k]) > max_sum:
                max_sum = sum(nums[i: i + k])
        k -= 1
    return max_sum
