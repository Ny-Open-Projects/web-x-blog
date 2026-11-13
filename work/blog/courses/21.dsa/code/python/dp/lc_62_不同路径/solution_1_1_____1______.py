# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def uniquePaths(m, n):  # 定义函数 uniquePaths（参数：映射表, 元素个数）
    # 计算组合数 C(m+n-2, m-1)，选择较小的那个计算以减少循环次数
    k = min(m - 1, n - 1)  # 把 取较小值 映射表 减 1, 元素个数 减 1) 存入 下标 k
    result = 1  # 把 1 存入 结果
    for i in range(1, k + 1):  # 让 下标 i 从 1 到 下标 k 加 1 遍历
        result *= m + n - 1 - i  # 把 (映射表 加 元素个数 减 1 减 下标 i) 写入 result *
        result //= i  # 确保每一步都是整数除法
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(uniquePaths(3, 7))  # 打印输出
