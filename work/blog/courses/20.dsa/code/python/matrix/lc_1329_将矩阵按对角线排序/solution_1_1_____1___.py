# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381786
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def diagonalSort(mat):  # 定义函数 diagonalSort（参数：mat）
    from collections import defaultdict  # from collections import defaultdict
    import heapq  # 引入依赖

    diagonals = defaultdict(list)  # 把 defaultdict(列表) 存入 diagonals
    rows, cols = len(mat), len(mat[0])  # 把 长度(mat), 长度(mat[0]) 写入 rows, cols
    for r in range(rows):  # 让 右指针 从 行数 遍历
        for c in range(cols):  # 让 字符 从 列数 遍历
            heapq.heappush(
                diagonals[r - c], mat[r][c]
            )  # heapq.heappush(diagonals[右指针 减 字符], mat[右指针][字符])
    for r in range(rows):  # 让 右指针 从 行数 遍历
        for c in range(cols):  # 让 字符 从 列数 遍历
            mat[r][c] = heapq.heappop(
                diagonals[r - c]
            )  # 把 heapq.heappop(diagonals[右指针 减 字符]) 写入 mat[r][c]
    return mat  # 返回 mat


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]  # 把 [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]] 存入 mat
    print(diagonalSort(mat))  # 打印输出
