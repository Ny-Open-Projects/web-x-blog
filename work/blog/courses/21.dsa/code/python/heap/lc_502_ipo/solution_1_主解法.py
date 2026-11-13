# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347672
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


def findMaximizedCapital(
    k, w, profits, capital
):  # 定义函数 findMaximizedCapital（参数：下标 k, 权重, profits, capital）
    n = len(profits)  # 把 长度(profits) 存入 元素个数
    # 按资本升序排列
    indices = sorted(range(n), key=lambda i: capital[i])
    # 最大堆（Python只有最小堆，用负数模拟）
    max_heap = []  # 把 [] 存入 max_heap
    i = 0  # 把 0 存入 下标 i
    for _ in range(k):  # 让 _ 从 下标 k 遍历
        # 将所有当前资本可以启动的项目加入最大堆
        while (
            i < n and capital[indices[i]] <= w
        ):  # 循环，直到不满足「下标 i 小于 元素个数 and capital[indices[下标 i]] 不超过 权重」
            heapq.heappush(
                max_heap, -profits[indices[i]]
            )  # heapq.heappush(max_heap, 减 profits[indices[下标 i]])
            i += 1  # 下标 i累加 1
        if not max_heap:  # 若 not max_heap
            break  # 跳出循环
        # 选择利润最大的项目
        w += -heapq.heappop(max_heap)  # 权重累加 减 heapq.heappop(max_heap)
    return w  # 返回 权重


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))  # 打印输出
