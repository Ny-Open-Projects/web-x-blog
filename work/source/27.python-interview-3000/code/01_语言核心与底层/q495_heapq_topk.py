import heapq
import itertools

if __name__ == "__main__":
    data = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print("largest 3:", heapq.nlargest(3, data))
    print("smallest 3:", heapq.nsmallest(3, data))

    heap = []                             # 流式 Top-3:小顶堆
    for x in data:
        heapq.heappush(heap, x)
        if len(heap) > 3:
            heapq.heappop(heap)
    print("top3 via heap:", sorted(heap, reverse=True))

    counter = itertools.count()           # 打破元组平局
    tasks = [(2, next(counter), "low"), (1, next(counter), "urgent"),
             (1, next(counter), "urgent2")]
    heapq.heapify(tasks)
    while tasks:
        print("run", heapq.heappop(tasks)[2])
