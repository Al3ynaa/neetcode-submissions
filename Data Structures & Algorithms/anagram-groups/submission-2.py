class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}

        for kelime in strs:
            key="".join(sorted(kelime))
            if key not in groups:
                groups[key]=[]
            groups[key].append(kelime)
        return list(groups.values())
            

            