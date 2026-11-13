# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134026430
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def spiralOrder(matrix):  # 定义函数 spiralOrder（参数：矩阵）
    if not matrix or not matrix[0]:  # 若 not 矩阵 or not 矩阵[0]
        return []  # 返回 []
    res = []  # 把 [] 存入 结果
    top, bottom = 0, len(matrix) - 1  # 把 0, 长度(矩阵) 减 1 写入 top, bottom
    left, right = 0, len(matrix[0]) - 1  # 把 0, 长度(矩阵[0]) 减 1 写入 left, right
    while top <= bottom and left <= right:  # 循环，直到不满足「top 不超过 bottom and 左边界 不超过 右边界」
        for j in range(left, right + 1):  # 让 下标 j 从 左边界 到 右边界 加 1 遍历
            res.append(matrix[top][j])  # 把 矩阵[top][下标 j] 追加到列表尾部
        top += 1  # top累加 1
        for i in range(top, bottom + 1):  # 让 下标 i 从 top 到 bottom 加 1 遍历
            res.append(matrix[i][right])  # 把 矩阵[下标 i][右边界] 追加到列表尾部
        right -= 1  # 右边界累减 1
        if top <= bottom:  # 若 top 不超过 bottom
            for j in range(right, left - 1, -1):  # 让 下标 j 从 右边界 到 左边界 减 1 到 减 1 遍历
                res.append(matrix[bottom][j])  # 把 矩阵[bottom][下标 j] 追加到列表尾部
            bottom -= 1  # bottom累减 1
        if left <= right:  # 若 左边界 不超过 右边界
            for i in range(bottom, top - 1, -1):  # 让 下标 i 从 bottom 到 top 减 1 到 减 1 遍历
                res.append(matrix[i][left])  # 把 矩阵[下标 i][左边界] 追加到列表尾部
            left += 1  # 左边界累加 1
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 打印输出
