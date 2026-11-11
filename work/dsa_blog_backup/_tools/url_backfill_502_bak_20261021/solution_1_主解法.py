import heapq

def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    # 按资本升序排列
    indices = sorted(range(n), key=lambda i: capital[i])
    # 最大堆（Python只有最小堆，用负数模拟）
    max_heap = []
    i = 0
    for _ in range(k):
        # 将所有当前资本可以启动的项目加入最大堆
        while i < n and capital[indices[i]] <= w:
            heapq.heappush(max_heap, -profits[indices[i]])
            i += 1
        if not max_heap:
            break
        # 选择利润最大的项目
        w += -heapq.heappop(max_heap)
    return w

if __name__ == '__main__':
    print(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
