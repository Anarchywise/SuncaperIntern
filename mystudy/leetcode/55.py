from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0  # 记录当前能够到达的最远位置

        for i in range(n):
            # 如果当前位置超过了当前能够到达的最远位置，说明无法到达最后一个位置
            if i > max_reach:
                return False

            # 更新当前能够到达的最远位置
            max_reach = max(max_reach, i + nums[i])

            # 如果最远位置已经超过或等于最后一个位置，说明可以到达
            if max_reach >= n - 1:
                return True

        return False

# 示例
nums = [2, 3, 1, 1, 4]
solution = Solution()
result = solution.canJump(nums)
print(result)

       