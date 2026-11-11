# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords(s):  # 定义函数 reverseWords（参数：字符串）
    def reverse_word(word):  # 定义函数 reverse_word（参数：单词）
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

    return " ".join(
        reverse_word(word) for word in s.split(" ")
    )  # 返回 ' '.join(reverse_word(单词) for 单词 in 字符串.split(' '))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords("Let's take LeetCode contest"))
