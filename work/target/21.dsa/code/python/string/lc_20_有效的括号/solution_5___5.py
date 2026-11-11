# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130442145
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isValid2(s):  # 定义函数 isValid2（参数：字符串）
    while (
        "()" in s or "{}" in s or "[]" in s
    ):  # 循环，直到不满足「'()' in 字符串 or '{}' in 字符串 or '[]' in 字符串」
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""  # 返回 字符串 等于 ''


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isValid2("abc"))  # 打印输出
