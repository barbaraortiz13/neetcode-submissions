class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:    

        counts = defaultdict(int)

        for x in nums:
            counts[x] +=1
        
        org = sorted(counts, key=counts.get, reverse=True)
        
        return [org[n] for n in range(k)]
        

