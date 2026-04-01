class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, arr: List[int], start: int, end: int):
        if end - start + 1 <= 1:
            return arr
        mid = (start + end) // 2

        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)

        self.merge(arr, start, mid, end)

    def merge(self, arr: List[int], start: int, mid: int, end: int):
        fp, sp = start, mid + 1

        res = []

        while fp <= mid and sp <= end:
            if arr[fp] > arr[sp]:
                res.append(arr[sp])
                # arr[fp], arr[sp] = arr[sp], arr[fp]
                sp += 1
            else:
                res.append(arr[fp])
                fp += 1

        while fp <= mid:
            res.append(arr[fp])
            fp += 1

        while sp <= end:
            res.append(arr[sp])
            sp += 1
        arr[start:end + 1] = res




