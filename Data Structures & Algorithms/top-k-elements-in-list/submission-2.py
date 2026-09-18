class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 0
        top_k = []
        sorted_data = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_data:
            top_k.append(key)
            if len(top_k) == k:
                return top_k
