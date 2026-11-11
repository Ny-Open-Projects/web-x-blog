# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def uniquePaths(m, n):  # 定义函数 uniquePaths（参数：映射表, 元素个数）
    f = [1] * n  # 把 [1] 乘 元素个数 存入 f
    for i in range(1, m):  # 让 下标 i 从 1 到 映射表 遍历
        for j in range(1, n):  # 让 下标 j 从 1 到 元素个数 遍历
            f[j] += f[j - 1]  # f[j]累加 f[下标 j 减 1]
    return f[n - 1]  # 返回 f[元素个数 减 1]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(uniquePaths(3, 7))  # 打印输出
