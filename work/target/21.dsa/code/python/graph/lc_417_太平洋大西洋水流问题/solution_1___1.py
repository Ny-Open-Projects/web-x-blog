# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133982215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def pacificAtlantic(matrix):  # 定义函数 pacificAtlantic（参数：矩阵）
    if not matrix or not matrix[0]:  # 若 not 矩阵 or not 矩阵[0]
        return []  # 返回 []
    rows, cols = len(matrix), len(matrix[0])  # 把 长度(矩阵), 长度(矩阵[0]) 写入 rows, cols
    pacific = [[False] * cols for _ in range(rows)]  # 把 [[False] 乘 列数 for _ in range(行数)] 存入 pacific
    atlantic = [
        [False] * cols for _ in range(rows)
    ]  # 把 [[False] 乘 列数 for _ in range(行数)] 存入 atlantic
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]  # 把 [(0, 1), (0, 减 1), (1, 0), ( 减 1, 0)] 存入 directions

    def dfs(r, c, visited):  # 定义函数 dfs（参数：右指针, 字符, 已访问集合）
        visited[r][c] = True  # 把 True 写入 visited[r][c]
        for dr, dc in directions:  # for dr, dc in directions:
            nr, nc = r + dr, c + dc  # 把 右指针 加 dr, 字符 加 dc 写入 nr, nc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and matrix[nr][nc] >= matrix[r][c]:
                dfs(nr, nc, visited)  # dfs(nr, nc, 已访问集合)

    for r in range(rows):  # 让 右指针 从 行数 遍历
        dfs(r, 0, pacific)  # dfs(右指针, 0, pacific)
        dfs(r, cols - 1, atlantic)  # dfs(右指针, 列数 减 1, atlantic)
    for c in range(cols):  # 让 字符 从 列数 遍历
        dfs(0, c, pacific)  # dfs(0, 字符, pacific)
        dfs(rows - 1, c, atlantic)  # dfs(行数 减 1, 字符, atlantic)
    result = []  # 把 [] 存入 结果
    for r in range(rows):  # 让 右指针 从 行数 遍历
        for c in range(cols):  # 让 字符 从 列数 遍历
            if pacific[r][c] and atlantic[r][c]:  # 若 pacific[右指针][字符] and atlantic[右指针][字符]
                result.append([r, c])  # 把 [右指针, 字符] 追加到列表尾部
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(pacificAtlantic(None))  # 打印输出
