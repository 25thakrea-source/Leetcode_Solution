
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_values = set(nums)
        result = 0

        for i in num_values:
            if i - 1 not in num_values:
                current = i
                length = 1

                while current + 1 in num_values:
                    current += 1
                    length += 1

                result = max(result, length)

        return result