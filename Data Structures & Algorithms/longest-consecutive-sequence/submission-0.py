class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        num_set=set(nums)
        for num in nums:
            if (num -1) not in num_set:
                counter=1
                next=num +1 
                while  next in num_set:
                    counter +=1
                    next +=1

                longest=max(longest,counter)
        return longest 