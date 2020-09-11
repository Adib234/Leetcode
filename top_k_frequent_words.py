class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        #         counter={}

        #         for word in words:
        #             counter[word]=counter.get(word,0)+1

        #         frequent = sorted(counter,key=lambda w:(-counter[w],w))

        #         return frequent[:k]

        counter = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
