# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145382034
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def myAtoi(s):  # 定义函数 myAtoi（参数：字符串）
    s = s.strip()  # 把 字符串.strip() 存入 字符串
    if not s:  # 若 not 字符串
        return 0  # 返回 0
    i = 0  # 把 0 存入 下标 i
    sign = 1  # 把 1 存入 sign
    if s[0] == "+":  # 若 字符串[0] 等于 ' 加 '
        i += 1  # 下标 i累加 1
    elif s[0] == "-":  # 否则，若 字符串[0] 等于 ' 减 '
        sign = -1  # 把 减 1 存入 sign
        i += 1  # 下标 i累加 1
    res = 0  # 把 0 存入 结果
    INT_MAX = 2**31 - 1  # 把 2 乘 乘 31 减 1 存入 INT_MAX
    while (
        i < len(s) and s[i].isdigit()
    ):  # 循环，直到不满足「下标 i 小于 长度(字符串) and 字符串[下标 i].isdigit(」
        digit = int(s[i])  # 把 int(字符串[下标 i]) 存入 digit
        if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else -INT_MAX - 1  # 返回 INT_MAX if sign 等于 1 else 减 INT_MAX 减 1
        res = res * 10 + digit  # 把 结果 乘 10 加 digit 存入 结果
        i += 1  # 下标 i累加 1
    return sign * res  # 返回 sign 乘 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(myAtoi("   -42"))  # 打印输出
    print(myAtoi("4193 with words"))  # 打印输出
    print(myAtoi("words and 987"))  # 打印输出
    print(myAtoi("-91283472332"))  # 打印输出
