class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict  = {}
        lst  = []
        for k in range(len(strs)):
          if strs[k] in lst:
            continue
          for str in strs:
            if(len(strs[k])== len(str) and self.check(strs[k],str)):
                if strs[k] not in dict.keys():
                    dict[strs[k]] = []
                dict[strs[k]].append(str)
                lst.append(str)
                
           

        res = []
        for k in dict.keys():
            if dict[k] not in res and dict[k]:
              res.append(dict[k])
        return (res)

    def check(self, s, t):
        return "".join(sorted(s)) == "".join(sorted(t))

            
        