import heapq
from collections import defaultdict

q = int(input())
heap = []
freq = defaultdict(int)

for _ in range(q):
    query = input().strip().split()
    if query[0] == '1':
        val = int(query[1])
        heapq.heappush(heap, val)
        freq[val] += 1

    elif query[0] == '2':
        val = int(query[1])
        if freq[val] > 0:
            freq[val] -= 1

    else:
        while heap and freq[heap[0]] == 0:
            heapq.heappop(heap)
        print(heap[0])
