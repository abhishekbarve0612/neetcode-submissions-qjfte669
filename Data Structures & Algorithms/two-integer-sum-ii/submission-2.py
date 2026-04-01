class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fp, sp = 0, len(numbers) - 1

        while fp < sp:
            csum = numbers[fp] + numbers[sp]
            if csum == target:
                return [fp + 1, sp + 1]
            elif csum > target:
                sp -= 1
            else:
                fp += 1

        return [-1, -1]
            