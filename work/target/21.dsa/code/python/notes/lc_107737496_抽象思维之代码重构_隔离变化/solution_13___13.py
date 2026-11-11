# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def match(regexp, text):  # 定义函数 match（参数：regexp, text）
    """扫描 text，若任一位置匹配 regexp 则返回 True（同 grep，方案 13）。"""
    if regexp and regexp[0] == "^":  # 若 regexp and regexp[0] 等于 ' 按位异或 '
        return matchhere(regexp[1:], text)  # 返回 matchhere(regexp[1:], text)
    i = 0  # 把 0 存入 下标 i
    while True:  # 循环，直到不满足「True」
        if matchhere(regexp, text[i:]):  # 若 matchhere(regexp, text[下标 i:]
            return True  # 返回 True
        if i >= len(text):  # 若 下标 i 不低于 长度(text
            break  # 跳出循环
        i += 1  # 下标 i累加 1
    return False  # 返回 False


def matchhere(regexp, text):  # 定义函数 matchhere（参数：regexp, text）
    if regexp == "":  # 若 regexp 等于 ''
        return True  # 返回 True
    if len(regexp) >= 2 and regexp[1] == "*":  # 若 长度(regexp) 不低于 2 and regexp[1] 等于 ' 乘 '
        return matchstar(regexp[0], regexp[2:], text)  # 返回 matchstar(regexp[0], regexp[2:], text)
    if regexp[0] == "$" and len(regexp) == 1:  # 若 regexp[0] 等于 '$' and 长度(regexp) 等于 1
        return text == ""  # 返回 text 等于 ''
    if text and (
        regexp[0] == "." or regexp[0] == text[0]
    ):  # 若 text and (regexp[0] 等于 '.' or regexp[0] 等于 text[0]
        return matchhere(regexp[1:], text[1:])  # 返回 matchhere(regexp[1:], text[1:])
    return False  # 返回 False


def matchstar(c, regexp, text):  # 定义函数 matchstar（参数：字符, regexp, text）
    i = 0  # 把 0 存入 下标 i
    while True:  # 循环，直到不满足「True」
        if matchhere(regexp, text[i:]):  # 若 matchhere(regexp, text[下标 i:]
            return True  # 返回 True
        if i >= len(text):  # 若 下标 i 不低于 长度(text
            break  # 跳出循环
        if text[i] != c and c != ".":  # 若 text[下标 i] 不等于 字符 and 字符 不等于 '.'
            break  # 跳出循环
        i += 1  # 下标 i累加 1
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(match("abc", "xxabcxx"))  # True
    print(match("a.c", "axc"))  # True
    print(match("a*", "aaaa"))  # True
    print(match("^a", "ba"))  # False
    print(match("c$", "abc"))  # True
    print(match("a.*c", "aXYZc"))  # True
