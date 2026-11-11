# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355461
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isAnagram(s, t):  # 定义函数 isAnagram（参数：字符串, 另一字符串）
    return sorted(s) == sorted(t)  # 返回 sorted(字符串) 等于 sorted(另一字符串)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isAnagram("anagram", "nagaram"))  # 打印输出
