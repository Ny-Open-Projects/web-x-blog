# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145380834
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minimumTime(n, relations, time):  # 定义函数 minimumTime（参数：元素个数, relations, time）
    from collections import defaultdict, deque  # from collections import defaultdict, deque

    graph = defaultdict(list)  # 把 defaultdict(列表) 存入 graph
    indeg = [0] * (n + 1)  # 把 [0] 乘 (元素个数 加 1) 存入 indeg
    for u, v in relations:  # for 节点 u, 值 in relations:
        graph[u].append(v)  # 把 值 追加到列表尾部
        indeg[v] += 1  # indeg[v]累加 1

    dp = [0] * (n + 1)  # 把 [0] 乘 (元素个数 加 1) 存入 DP 表
    for i in range(1, n + 1):  # 让 下标 i 从 1 到 元素个数 加 1 遍历
        dp[i] = time[i - 1]  # 把 time[下标 i 减 1] 写入 dp[i]

    q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
    while q:  # 循环，直到不满足「节点」
        u = q.popleft()  # 把 节点.popleft() 存入 节点 u
        for v in graph[u]:  # 逐个取出 graph 的元素（值）
            dp[v] = max(
                dp[v], dp[u] + time[v - 1]
            )  # 把 取较大值 DP 表[值], DP 表[节点 u] 加 time[值 减 1]) 写入 dp[v]
            indeg[v] -= 1  # indeg[v]累减 1
            if indeg[v] == 0:  # 若 indeg[值] 等于 0
                q.append(v)  # 把 值 追加到列表尾部

    return max(dp)  # 返回 取较大值 DP 表)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))  # 打印输出
