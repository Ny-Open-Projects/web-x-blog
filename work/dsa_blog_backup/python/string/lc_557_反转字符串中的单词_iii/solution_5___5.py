# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords3(s):  # 定义函数 reverseWords3（参数：字符串）
    if not s:  # 若 not 字符串
        return ""  # 返回 ''
    return " ".join(
        word[::-1] for word in s.split(" ")
    )  # 返回 ' '.join(单词[:: 减 1] for 单词 in 字符串.split(' '))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords3("Let's take LeetCode contest"))
