# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116781
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseString(s):  # 定义函数 reverseString（参数：字符串）
    n = len(s)  # 把 长度(字符串) 存入 元素个数
    for left in range(n // 2):  # 让 左边界 从 元素个数 除以 除以 2 遍历
        right = n - 1 - left  # 把 元素个数 减 1 减 左边界 存入 右边界
        s[left], s[right] = s[right], s[left]  # 把 字符串[右边界], 字符串[左边界] 写入 s[left], s[right]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = list("abc")  # 把 列表(「abc」) 存入 字符串
    reverseString(s)  # reverseString(字符串)
    print("".join(s))  # 打印输出
    s2 = list("hello")  # 把 列表(「hello」) 存入 s2
    reverseString(s2)  # reverseString(s2)
    print("".join(s2))  # 打印输出
