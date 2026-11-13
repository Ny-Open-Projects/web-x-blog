# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords4(s):  # 定义函数 reverseWords4（参数：字符串）
    if not s:  # 若 not 字符串
        return ""  # 返回 ''
    import re  # 引入依赖

    return " ".join(item[::-1] for item in re.findall(r"[\w']+", s))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords4("Let's take LeetCode contest"))
