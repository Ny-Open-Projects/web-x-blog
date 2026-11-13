# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130414333
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseWords(s):  # 定义函数 reverseWords（参数：字符串）
    words = s.split(" ")  # 把 字符串.split(' ') 存入 单词列表
    for i in range(len(words)):  # 让 下标 i 从 长度(单词列表 遍历
        words[i] = words[i][::-1]  # 把 单词列表[下标 i][:: 减 1] 写入 words[i]
    return " ".join(words)  # 返回 ' '.join(单词列表)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseWords("Let's take LeetCode contest"))
