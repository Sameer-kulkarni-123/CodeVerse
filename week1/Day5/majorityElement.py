class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        maj = len(nums)//2

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if num not in dct.keys():
                dct[num] = 1
            else:
                dct[num] += 1
                if dct[num] > maj:
                    return num