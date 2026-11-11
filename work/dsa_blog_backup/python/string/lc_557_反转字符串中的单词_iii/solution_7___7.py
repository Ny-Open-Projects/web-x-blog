# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords5(s):  # 定义函数 reverseWords5（参数：字符串）
    words = s.split(" ")  # 把 字符串.split(' ') 存入 单词列表
    for i in range(len(words)):  # 让 下标 i 从 长度(单词列表 遍历
        words[i] = reverseWord(words[i])  # 把 reverseWord(单词列表[下标 i]) 写入 words[i]
    return " ".join(words)  # 返回 ' '.join(单词列表)


def reverseWord(word):  # 定义函数 reverseWord（参数：单词）
    chars = list(word)  # 把 列表(单词) 存入 chars
    left, right = 0, len(chars) - 1  # 把 0, 长度(chars) 减 1 写入 left, right
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        chars[left], chars[right] = (
            chars[right],
            chars[left],
        )  # 把 chars[右边界], chars[左边界] 写入 chars[left], chars[right]
        left += 1  # 左边界累加 1
        right -= 1  # 右边界累减 1
    return "".join(chars)  # 返回 ''.join(chars)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords5("Let's take LeetCode contest"))
