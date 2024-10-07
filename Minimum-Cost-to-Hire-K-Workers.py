class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # Overall time complexity is O(nlogn + nlogk)
        res = float("inf")

        pairs = [] #(ratio, quality)
        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))
        pairs.sort(key=lambda p:p[0]) #this sorts the ratios

        maxHeap = [] #qualities
        total_quality = 0 # quality never changes for each individual person, the wage does

        for rate, q in pairs:
            heapq.heappush(maxHeap, -q) #note that heaps are only implemented as minimum heaps, therefore we add the negative of the quality
            total_quality += q

            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)

            if len(maxHeap) == k:
                res = min(
                    res,
                    total_quality * rate  
                )

        return res