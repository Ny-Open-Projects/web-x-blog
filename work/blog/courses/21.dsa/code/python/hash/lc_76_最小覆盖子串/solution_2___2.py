# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133465616
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minWindow(s, t):  # 定义函数 minWindow（参数：字符串, 另一字符串）
    from collections import Counter  # from collections import Counter

    need = Counter(t)  # 把 Counter(另一字符串) 存入 need
    m_size = len(need)  # 把 长度(need) 存入 m_size
    l = 0  # 把 0 存入 左指针
    res = ""  # 把 '' 存入 结果
    for r in range(len(s)):  # 让 右指针 从 长度(字符串 遍历
        c = s[r]  # 把 字符串[右指针] 存入 字符
        if c in need:  # 若 字符 in need
            need[c] -= 1  # need[c]累减 1
            if need[c] == 0:  # 若 need[字符] 等于 0
                m_size -= 1  # m_size累减 1
        while m_size == 0:  # 循环，直到不满足「m_size 等于 0」
            new_res = s[l : r + 1]  # 把 字符串[左指针:右指针 加 1] 存入 new_res
            if not res or len(new_res) < len(res):  # 若 not 结果 or 长度(new_res) 小于 长度(结果
                res = new_res  # 把 new_res 存入 结果
            c2 = s[l]  # 把 字符串[左指针] 存入 c2
            if c2 in need:  # 若 c2 in need
                need[c2] += 1  # need[c2]累加 1
                if need[c2] == 1:  # 若 need[c2] 等于 1
                    m_size += 1  # m_size累加 1
            l += 1  # 左指针累加 1
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minWindow("ADOBECODEBANC", "ABC"))  # 打印输出
    print(minWindow("a", "a"))  # 打印输出
    print(minWindow("a", "aa"))  # 打印输出
