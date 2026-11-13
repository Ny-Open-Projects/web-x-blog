# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords(s):  # 定义函数 reverseWords（参数：字符串）
    return " ".join(s.strip().split()[::-1])  # 返回 「 」.join(字符串.strip().split()[:: 减 1])


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords("abc"))  # 打印输出
