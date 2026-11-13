# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144847773
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def uniquePaths(m, n):  # 定义函数 uniquePaths（参数：映射表, 元素个数）
    # 组合优化版：C(m+n-2, m-1)
    ans = 1  # 把 1 存入 答案
    x = n  # 把 元素个数 存入 x
    y = 1  # 把 1 存入 y
    while y < m:  # 循环，直到不满足「y 小于 映射表」
        ans = ans * x // y  # 把 答案 乘 x 除以 除以 y 存入 答案
        x += 1  # x累加 1
        y += 1  # y累加 1
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(uniquePaths(3, 7))  # 打印输出
