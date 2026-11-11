# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minFlipsMonoIncr(s):  # 定义函数 minFlipsMonoIncr（参数：字符串）
    n = len(s)  # 把 长度(字符串) 存入 元素个数
    dp0 = 0  # 把 0 存入 dp0
    dp1 = 0  # 把 0 存入 dp1
    for i in range(n):  # 让 下标 i 从 元素个数 遍历
        c = s[i]  # 把 字符串[下标 i] 存入 字符
        dp0New = dp0  # 把 dp0 存入 dp0New
        dp1New = min(dp0, dp1)  # 把 取较小值 dp0, dp1) 存入 dp1New
        if c == "1":  # 若 字符 等于 '1'
            dp0New += 1  # dp0New累加 1
        else:  # 否则
            dp1New += 1  # dp1New累加 1
        dp0 = dp0New  # 把 dp0New 存入 dp0
        dp1 = dp1New  # 把 dp1New 存入 dp1
    return min(dp0, dp1)  # 返回 取较小值 dp0, dp1)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minFlipsMonoIncr("00110"))  # 打印输出
