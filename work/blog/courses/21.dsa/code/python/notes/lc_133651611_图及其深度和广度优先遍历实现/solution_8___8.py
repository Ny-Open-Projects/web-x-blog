# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
graph = {  # 把 { 存入 graph
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3],
}


def bfs(start):  # 定义函数 bfs（参数：起点）
    res = []  # 把 [] 存入 结果
    visited = set()  # 把 set() 存入 已访问集合
    q = [start]  # 把 [起点] 存入 节点
    visited.add(start)  # 已访问集合 追加 起点)
    while q:  # 循环，直到不满足「节点」
        n = q.pop(0)  # 把 节点 弹出 0) 存入 元素个数
        res.append(n)  # 把 元素个数 追加到列表尾部
        for c in graph[n]:  # 逐个取出 graph 的元素（字符）
            if c not in visited:  # 若 字符 not in 已访问集合
                q.append(c)  # 把 字符 追加到列表尾部
                visited.add(c)  # 已访问集合 追加 字符)
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    print(",".join(map(str, bfs(2))))  # 打印输出
