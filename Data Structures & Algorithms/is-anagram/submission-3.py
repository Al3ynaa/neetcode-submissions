class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS={}
        countT={}
        for harf in s:
            countS[harf] = countS.get(harf, 0) + 1
        for harf in t:
            countT[harf] = countT.get(harf, 0) + 1
        return countS==countT