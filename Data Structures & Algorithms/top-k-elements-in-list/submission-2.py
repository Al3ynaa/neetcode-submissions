class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]= 1
        ordered=sorted(count.items(),reverse=True, key=lambda item:item[1])
        result=[]
        for t in ordered[:k]:
            result.append(t[0])
        return result