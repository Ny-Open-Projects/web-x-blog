# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def countBinarySubstrings2(s):  # 定义函数 countBinarySubstrings2（参数：字符串）
    prev, curr = 0, 1  # 把 0, 1 写入 prev, curr
    res = 0  # 把 0 存入 结果
    for i in range(1, len(s)):  # 让 下标 i 从 1 到 长度(字符串 遍历
        if s[i] != s[i - 1]:  # 若 字符串[下标 i] 不等于 字符串[下标 i 减 1]
            res += min(prev, curr)  # 结果累加 取较小值 前一个, 当前值)
            prev, curr = curr, 1  # 把 当前值, 1 写入 prev, curr
        else:  # 否则
            curr += 1  # 当前值累加 1
    return res + min(prev, curr)  # 返回 结果 加 取较小值 前一个, 当前值)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(countBinarySubstrings2("abc"))  # 打印输出
