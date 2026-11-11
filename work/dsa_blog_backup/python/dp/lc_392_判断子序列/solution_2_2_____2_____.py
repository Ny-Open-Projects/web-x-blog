# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSubsequence(s, t):  # 定义函数 isSubsequence（参数：字符串, 另一字符串）
    # 双指针
    n = len(s)  # 把 长度(字符串) 存入 元素个数
    m = len(t)  # 把 长度(另一字符串) 存入 映射表
    i = 0  # 把 0 存入 下标 i
    j = 0  # 把 0 存入 下标 j
    while i < n and j < m:  # 循环，直到不满足「下标 i 小于 元素个数 and 下标 j 小于 映射表」
        if s[i] == t[j]:  # 若 字符串[下标 i] 等于 另一字符串[下标 j]
            i += 1  # 下标 i累加 1
        j += 1  # 下标 j累加 1
    return i == n  # 返回 下标 i 等于 元素个数


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSubsequence("abc", "ahbgdc"))  # 打印输出
