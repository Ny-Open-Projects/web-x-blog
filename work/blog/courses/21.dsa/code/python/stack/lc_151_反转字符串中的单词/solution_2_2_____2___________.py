# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def trimSpaces(s):  # 定义函数 trimSpaces（参数：字符串）
    left, right = 0, len(s) - 1  # 把 0, 长度(字符串) 减 1 写入 left, right
    while (
        left <= right and s[left] == " "
    ):  # 循环，直到不满足「左边界 不超过 右边界 and 字符串[左边界] 等于 ' '」
        left += 1  # 左边界累加 1
    while (
        left <= right and s[right] == " "
    ):  # 循环，直到不满足「左边界 不超过 右边界 and 字符串[右边界] 等于 ' '」
        right -= 1  # 右边界累减 1
    output = []  # 把 [] 存入 输出
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        if s[left] != " ":  # 若 字符串[左边界] 不等于 ' '
            output.append(s[left])  # 把 字符串[左边界] 追加到列表尾部
        elif output and output[-1] != " ":  # 否则，若 输出 and 输出[ 减 1] 不等于 ' '
            output.append(s[left])  # 把 字符串[左边界] 追加到列表尾部
        left += 1  # 左边界累加 1
    return output  # 返回 输出


def reverse(l, left, right):  # 定义函数 reverse（参数：左指针, 左边界, 右边界）
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        l[left], l[right] = l[right], l[left]  # 把 左指针[右边界], 左指针[左边界] 写入 l[left], l[right]
        left += 1  # 左边界累加 1
        right -= 1  # 右边界累减 1


def reverseEachWord(l):  # 定义函数 reverseEachWord（参数：左指针）
    n = len(l)  # 把 长度(左指针) 存入 元素个数
    start = end = 0  # 把 终点 赋值为 0 存入 起点
    while start < n:  # 循环，直到不满足「起点 小于 元素个数」
        while end < n and l[end] != " ":  # 循环，直到不满足「终点 小于 元素个数 and 左指针[终点] 不等于 ' '」
            end += 1  # 终点累加 1
        reverse(l, start, end - 1)  # reverse(左指针, 起点, 终点 减 1)
        start = end + 1  # 把 终点 加 1 存入 起点
        end = start  # 把 起点 存入 终点


def reverseWords(s):  # 定义函数 reverseWords（参数：字符串）
    l = trimSpaces(s)  # 把 trimSpaces(字符串) 存入 左指针
    reverse(l, 0, len(l) - 1)  # reverse(左指针, 0, 长度(左指针) 减 1)
    reverseEachWord(l)  # reverseEachWord(左指针)
    return "".join(l)  # 返回 「」.join(左指针)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(trimSpaces("abc"))  # 打印输出
