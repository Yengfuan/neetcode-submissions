class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        data = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        res = []
        for i in data:
            res.append(i)
            if len(res) >= k:
                return res
            

        