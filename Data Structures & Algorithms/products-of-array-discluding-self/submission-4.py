class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        zero_cnt = 0
        prod = 1

        for i in range(n):
            if nums[i] == 0:
                zero_cnt += 1
            else:
                prod *= nums[i]
        
        if zero_cnt > 1:
            return [0] * n
    
        for j in range(n):
            if zero_cnt == 1:
                if nums[j] == 0:
                    output[j] = prod
            if zero_cnt == 0:
                output[j] = prod // nums[j]

        return output