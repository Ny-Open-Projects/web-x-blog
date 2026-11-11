# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660487
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def climbStairs(n):  # 定义函数 climbStairs（参数：元素个数）
    # 迭代生成（生成器累计）
    a, b = 1, 1  # 把 1, 1 写入 a, b
    for _ in range(n):  # 让 _ 从 元素个数 遍历
        a, b = b, a + b  # 把 b, 数组 加 b 写入 a, b
    return a  # 返回 数组


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(climbStairs(5))  # 打印输出
