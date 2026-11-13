# 来源（blog）：LeetCode 58. 最后一个单词的长度 — 方案1：从尾部扫描（split 取末词）
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def length_of_last_word(s):  # 定义函数 length_of_last_word（参数：字符串）
    trimmed = s.strip()  # 把 字符串.strip() 存入 trimmed
    if trimmed == "":  # 若 trimmed 等于 「」
        return 0  # 返回 0
    parts = trimmed.split()  # 把 trimmed.split() 存入 parts
    return len(parts[-1])  # 返回 长度(parts[ 减 1])


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ]
    for inp, want in cases:  # for inp, want in cases:
        got = length_of_last_word(inp)  # 把 length_of_last_word(inp) 存入 got
        assert got == want, f"lengthOfLastWord({inp!r}) = {got}, want {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
