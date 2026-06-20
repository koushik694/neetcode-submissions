class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_n={}
        for num in nums:
            if num in count_n:
                count_n[num]+=1
            else:
                count_n[num]=1
        return sorted(count_n,key= lambda x:count_n[x],reverse=True)[:k]
        