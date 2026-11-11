# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133461048
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lengthOfLongestSubstring(s):  # 定义函数 lengthOfLongestSubstring（参数：字符串）
    last = {}  # 把 {} 存入 last
    l = 0  # 把 0 存入 左指针
    res = 0  # 把 0 存入 结果
    for r, ch in enumerate(s):  # 同时取 右指针 与 字符 遍历
        if ch in last and last[ch] >= l:  # 若 字符 in last and last[字符] 不低于 左指针
            l = last[ch] + 1  # 把 last[字符] 加 1 存入 左指针
        res = max(res, r - l + 1)  # 把 取较大值 结果, 右指针 减 左指针 加 1) 存入 结果
        last[ch] = r  # 把 右指针 写入 last[ch]
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lengthOfLongestSubstring("abcabcbb"))  # 打印输出
    print(lengthOfLongestSubstring("bbbbb"))  # 打印输出
    print(lengthOfLongestSubstring("pwwkew"))  # 打印输出
