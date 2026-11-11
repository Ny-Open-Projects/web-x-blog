# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133920771
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isNumber(s):  # 定义函数 isNumber（参数：字符串）
    s = s.strip()  # 把 字符串.strip() 存入 字符串
    if not s:  # 若 not 字符串
        return False  # 返回 False
    has_dot = has_e = has_digit = False  # 把 has_e 赋值为 has_digit 赋值为 False 存入 has_dot
    for i, c in enumerate(s):  # 同时取 下标 i 与 字符 遍历
        if c == ".":  # 若 字符 等于 '.'
            if has_dot or has_e:  # 若 has_dot or has_e
                return False  # 返回 False
            has_dot = True  # 把 True 存入 has_dot
        elif c == "e" or c == "E":  # 否则，若 字符 等于 'e' or 字符 等于 'E'
            if has_e or not has_digit:  # 若 has_e or not has_digit
                return False  # 返回 False
            has_e = True  # 把 True 存入 has_e
            has_digit = False  # 把 False 存入 has_digit
        elif c == "+" or c == "-":  # 否则，若 字符 等于 ' 加 ' or 字符 等于 ' 减 '
            if i > 0 and s[i - 1] not in "eE":  # 若 下标 i 超过 0 and 字符串[下标 i 减 1] not in 'eE'
                return False  # 返回 False
        elif c.isdigit():  # 否则，若 字符.isdigit(
            has_digit = True  # 把 True 存入 has_digit
        else:  # 否则
            return False  # 返回 False
    return has_digit  # 返回 has_digit


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isNumber("abc"))  # 打印输出
