class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for st in strs:
            sort = "".join(sorted(st))
            if sort not in group.keys():
                group[sort] = []
            group[sort].append(st)                
        
        return list(group.values())
