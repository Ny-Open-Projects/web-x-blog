# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116781
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseString(s):  # 定义函数 reverseString（参数：字符串）
    left, right = 0, len(s) - 1  # 把 0, 长度(字符串) 减 1 写入 left, right
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        s[left], s[right] = s[right], s[left]  # 把 字符串[右边界], 字符串[左边界] 写入 s[left], s[right]
        left += 1  # 左边界累加 1
        right -= 1  # 右边界累减 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    s = list("abc")  # 把 列表(「abc」) 存入 字符串
    reverseString(s)  # reverseString(字符串)
    print("".join(s))  # 打印输出
    s2 = list("hello")  # 把 列表(「hello」) 存入 s2
    reverseString(s2)  # reverseString(s2)
    print("".join(s2))  # 打印输出
