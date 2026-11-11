# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def pacificAtlantic(matrix):  # 定义函数 pacificAtlantic（参数：矩阵）
    if not matrix or not matrix[0]:  # 若 not 矩阵 or not 矩阵[0]
        return []  # 返回 []
    m, n = len(matrix), len(matrix[0])  # 把 长度(矩阵), 长度(矩阵[0]) 写入 m, n
    pacific = [[False] * n for _ in range(m)]  # 把 [[False] 乘 元素个数 for _ in range(映射表)] 存入 pacific
    atlantic = [
        [False] * n for _ in range(m)
    ]  # 把 [[False] 乘 元素个数 for _ in range(映射表)] 存入 atlantic

    def dfs(r, c, flow):  # 定义函数 dfs（参数：右指针, 字符, flow）
        flow[r][c] = True  # 把 True 写入 flow[r][c]
        for dr, dc in (
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ):  # for dr, dc in (( 减 1, 0), (1, 0), (0, 减 1), (0, 1)):
            nr, nc = r + dr, c + dc  # 把 右指针 加 dr, 字符 加 dc 写入 nr, nc
            if 0 <= nr < m and 0 <= nc < n and not flow[nr][nc] and matrix[nr][nc] >= matrix[r][c]:
                dfs(nr, nc, flow)  # dfs(nr, nc, flow)

    for r in range(m):  # 让 右指针 从 映射表 遍历
        dfs(r, 0, pacific)  # dfs(右指针, 0, pacific)
        dfs(r, n - 1, atlantic)  # dfs(右指针, 元素个数 减 1, atlantic)
    for c in range(n):  # 让 字符 从 元素个数 遍历
        dfs(0, c, pacific)  # dfs(0, 字符, pacific)
        dfs(m - 1, c, atlantic)  # dfs(映射表 减 1, 字符, atlantic)

    res = []  # 把 [] 存入 结果
    for r in range(m):  # 让 右指针 从 映射表 遍历
        for c in range(n):  # 让 字符 从 元素个数 遍历
            if pacific[r][c] and atlantic[r][c]:  # 若 pacific[右指针][字符] and atlantic[右指针][字符]
                res.append([r, c])  # 把 [右指针, 字符] 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(
        pacificAtlantic(
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    )  # ]))
