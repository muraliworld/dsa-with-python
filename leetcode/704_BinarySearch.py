from typing import List


class Solution:
    def search( nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        return -1


data = [-9,8,3,4,12,29,33,39,43]
t = 33;

print(Solution.search(data,t))
