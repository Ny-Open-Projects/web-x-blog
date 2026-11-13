# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144852792
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isSubsequence(s, t):  # 定义函数 isSubsequence（参数：字符串, 另一字符串）
    i = 0  # 把 0 存入 下标 i
    for j in range(len(t)):  # 让 下标 j 从 长度(另一字符串 遍历
        if (
            i < len(s) and s[i] == t[j]
        ):  # 若 下标 i 小于 长度(字符串) and 字符串[下标 i] 等于 另一字符串[下标 j]
            i += 1  # 下标 i累加 1
    return i == len(s)  # 返回 下标 i 等于 长度(字符串)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isSubsequence("abc", "ahbgdc"))  # 打印输出
