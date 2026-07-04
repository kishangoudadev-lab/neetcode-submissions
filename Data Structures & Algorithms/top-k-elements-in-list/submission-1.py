class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = dict()
        res = []
        for num in nums:
            if num not in group:
                group[num] = 0 
            group[num]+=1

        sorted_keys = sorted(group, key=group.get, reverse=True)
        res = sorted_keys[:k]
        return res
