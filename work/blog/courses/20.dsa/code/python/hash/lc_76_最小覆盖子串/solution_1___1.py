# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minWindow(s, t):  # 定义函数 minWindow（参数：字符串, 另一字符串）
    from collections import Counter  # from collections import Counter

    if not s or not t:  # 若 not 字符串 or not 另一字符串
        return ""  # 返回 「」
    target_count = Counter(t)  # 把 Counter(另一字符串) 存入 target_count
    required = len(target_count)  # 引入依赖
    left = right = 0  # 把 右边界 赋值为 0 存入 左边界
    formed = 0  # 把 0 存入 formed
    window_count = {}  # 把 {} 存入 window_count
    min_len = float("inf")  # 把 float('inf') 存入 min_len
    min_left = 0  # 把 0 存入 min_left
    while right < len(s):  # 循环，直到不满足「右边界 小于 长度(字符串」
        char = s[right]  # 把 字符串[右边界] 存入 char
        window_count[char] = (
            window_count.get(char, 0) + 1
        )  # 把 window_count 查找 char, 0) 加 1 写入 window_count[char]
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1  # formed累加 1
        while (
            left <= right and formed == required
        ):  # 循环，直到不满足「左边界 不超过 右边界 and formed 等于 required」
            char = s[left]  # 把 字符串[左边界] 存入 char
            if right - left + 1 < min_len:  # 若 右边界 减 左边界 加 1 小于 min_len
                min_len = right - left + 1  # 把 右边界 减 左边界 加 1 存入 min_len
                min_left = left  # 把 左边界 存入 min_left
            window_count[char] -= 1  # window_count[char]累减 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1  # formed累减 1
            left += 1  # 左边界累加 1
        right += 1  # 右边界累加 1
    return "" if min_len == float("inf") else s[min_left : min_left + min_len]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minWindow("abc", None))  # 打印输出
