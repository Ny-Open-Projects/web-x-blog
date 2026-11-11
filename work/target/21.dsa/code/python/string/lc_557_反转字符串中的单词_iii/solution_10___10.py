# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords(s):  # 定义函数 reverseWords（参数：字符串）
    chars = list(s)  # 把 列表(字符串) 存入 chars
    n = len(chars)  # 把 长度(chars) 存入 元素个数
    i = 0  # 把 0 存入 下标 i
    while i < n:  # 循环，直到不满足「下标 i 小于 元素个数」
        if chars[i] == " ":  # 若 chars[下标 i] 等于 ' '
            i += 1  # 下标 i累加 1
            continue  # 跳过本轮，进入下一次
        j = i  # 把 下标 i 存入 下标 j
        while (
            j < n and chars[j] != " "
        ):  # 循环，直到不满足「下标 j 小于 元素个数 and chars[下标 j] 不等于 ' '」
            j += 1  # 下标 j累加 1
        left, right = i, j - 1  # 把 下标 i, 下标 j 减 1 写入 left, right
        while left < right:  # 循环，直到不满足「左边界 小于 右边界」
            chars[left], chars[right] = (
                chars[right],
                chars[left],
            )  # 把 chars[右边界], chars[左边界] 写入 chars[left], chars[right]
            left += 1  # 左边界累加 1
            right -= 1  # 右边界累减 1
        i = j  # 把 下标 j 存入 下标 i
    return "".join(chars)  # 返回 ''.join(chars)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords("Let's take LeetCode contest"))
