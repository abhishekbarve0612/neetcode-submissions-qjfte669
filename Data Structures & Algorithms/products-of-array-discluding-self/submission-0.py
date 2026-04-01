class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        leftProducts = [1] * (l + 1)
        rightProducts = [1] * (l + 1)
        for idx in range(1, l + 1):
            leftProducts[idx] = nums[idx - 1] * leftProducts[idx - 1]
            rightProducts[idx] = nums[l - idx] * rightProducts[idx - 1]
        products = [1] * l
        leftProducts = leftProducts[1:]
        rightProducts = rightProducts[::-1][:-1]
        products[0] = rightProducts[1]
        products[-1] = leftProducts[-2]
        print(products)
        for idx in range(1, l - 1):
            products[idx] = leftProducts[idx - 1] * rightProducts[idx + 1]
        # products.append(leftProducts[-2])
        return products