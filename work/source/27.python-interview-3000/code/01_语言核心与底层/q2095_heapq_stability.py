"""heapq 没有稳定性:相等键的出堆顺序不可依赖。"""
import heapq


letters = [("z", 1), ("y", 1), ("x", 1), ("w", 1)]


if __name__ == "__main__":
    plain = []
    for name, priority in letters:
        heapq.heappush(plain, (priority, name))
    print("入堆顺序:", [n for n, _ in letters])
    print("裸堆出队:", [name for _, name in [heapq.heappop(plain) for _ in range(4)]])

    indexed = []
    for idx, (name, priority) in enumerate(letters):
        heapq.heappush(indexed, (priority, idx, name))
    print("带序号出队:", [name for _, _, name in [heapq.heappop(indexed) for _ in range(4)]])

    class Task:
        pass

    heap3 = [(1, 0, "a"), (1, 1, "b")]
    heapq.heapify(heap3)
    try:
        heapq.heappush(heap3, (1, Task()))     # 漏掉序号:平局时比较对象本身
    except TypeError as e:
        print("同优先级缺序号:", str(e)[:48])
