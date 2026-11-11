# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133651611
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
graph = {  # 把 { 存入 graph
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3],
}


def dfs(n, visited, res):  # 定义函数 dfs（参数：元素个数, 已访问集合, 结果）
    res.append(n)  # 把 元素个数 追加到列表尾部
    visited.add(n)  # 已访问集合 追加 元素个数)
    for c in graph[n]:  # 逐个取出 graph 的元素（字符）
        if c not in visited:  # 若 字符 not in 已访问集合
            dfs(c, visited, res)  # dfs(字符, 已访问集合, 结果)


if __name__ == "__main__":  # 若 __name__ 等于 「__main__」
    visited = set()  # 把 set() 存入 已访问集合
    res = []  # 把 [] 存入 结果
    dfs(2, visited, res)  # dfs(2, 已访问集合, 结果)
    print(",".join(map(str, res)))  # 打印输出
