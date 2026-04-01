class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers) - 1

        while first < last:
            current_sum = numbers[first] + numbers[last]

            if current_sum == target:
                return [first + 1, last + 1]

            if current_sum > target:
                last -= 1

            else:
                first += 1

        return [-1, -1]