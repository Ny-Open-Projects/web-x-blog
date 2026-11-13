# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133461048
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lengthOfLongestSubstring(s):  # 定义函数 lengthOfLongestSubstring（参数：字符串）
    char_set = set()  # 把 set() 存入 char_set
    left = 0  # 把 0 存入 左边界
    max_len = 0  # 把 0 存入 max_len
    for right in range(len(s)):  # 让 右边界 从 长度(字符串 遍历
        while s[right] in char_set:  # 循环，直到不满足「字符串[右边界] in char_set」
            char_set.remove(s[left])  # char_set 弹出 字符串[左边界])
            left += 1  # 左边界累加 1
        char_set.add(s[right])  # char_set 追加 字符串[右边界])
        max_len = max(max_len, right - left + 1)  # 把 取较大值 max_len, 右边界 减 左边界 加 1) 存入 max_len
    return max_len  # 返回 max_len


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lengthOfLongestSubstring("abc"))  # 打印输出
