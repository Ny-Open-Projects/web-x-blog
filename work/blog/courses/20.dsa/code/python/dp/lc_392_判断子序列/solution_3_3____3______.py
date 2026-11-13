# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSubsequence(s, t):  # 定义函数 isSubsequence（参数：字符串, 另一字符串）
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSubsequence("abc", None))  # 打印输出
