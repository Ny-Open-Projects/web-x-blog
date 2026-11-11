# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


def nthSuperUglyNumber(n, primes):  # 定义函数 nthSuperUglyNumber（参数：元素个数, primes）
    # 用最小堆维护各个素数指针产生的候选值，弹出时跳过与上一个相同（重复）的值
    ugly = [1] * n  # 把 [1] 乘 元素个数 存入 ugly
    p = [0] * len(primes)  # 每个素数在 ugly 中的指针
    heap = [
        (primes[j], j) for j in range(len(primes))
    ]  # 把 [(primes[下标 j], 下标 j) for 下标 j in range(长度(primes))] 存入 堆
    heapq.heapify(heap)  # heapq.heapify(堆)
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        val, j = heapq.heappop(heap)  # 把 heapq.heappop(堆) 写入 val, j
        while val == ugly[i - 1]:  # 循环，直到不满足「值 等于 ugly[下标 i 减 1]」
            p[j] += 1  # p[j]累加 1
            heapq.heappush(
                heap, (ugly[p[j]] * primes[j], j)
            )  # heapq.heappush(堆, (ugly[节点[下标 j]] 乘 primes[下标 j], 下标 j))
            val, j = heapq.heappop(heap)  # 把 heapq.heappop(堆) 写入 val, j
        ugly[i] = val  # 把 值 写入 ugly[i]
        p[j] += 1  # p[j]累加 1
        heapq.heappush(
            heap, (ugly[p[j]] * primes[j], j)
        )  # heapq.heappush(堆, (ugly[节点[下标 j]] 乘 primes[下标 j], 下标 j))
    return ugly[-1]  # 返回 ugly[ 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(nthSuperUglyNumber(12, [2, 7, 13, 19]))  # 打印输出
