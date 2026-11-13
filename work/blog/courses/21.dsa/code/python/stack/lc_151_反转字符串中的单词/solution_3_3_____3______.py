# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113405
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords(s):  # 定义函数 reverseWords（参数：字符串）
    left, right = 0, len(s) - 1  # 把 0, 长度(字符串) 减 1 写入 left, right
    words = []  # 把 [] 存入 单词列表
    word = []  # 把 [] 存入 单词
    while left <= right:  # 循环，直到不满足「左边界 不超过 右边界」
        if s[left] == " " and word:  # 若 字符串[左边界] 等于 ' ' and 单词
            words.insert(0, "".join(word))  # 拼接为字符串
            word = []  # 把 [] 存入 单词
        elif s[left] != " ":  # 否则，若 字符串[左边界] 不等于 ' '
            word.append(s[left])  # 把 字符串[左边界] 追加到列表尾部
        left += 1  # 左边界累加 1
    if word:  # 若 单词
        words.insert(0, "".join(word))  # 拼接为字符串
    return " ".join(words)  # 返回 「 」.join(单词列表)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords("abc"))  # 打印输出
