# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145381295
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def onesCount(x):  # 定义函数 onesCount（参数：x）
    c = 0  # 把 0 存入 字符
    while x > 0:  # 循环，直到不满足「x 超过 0」
        c += x % 2  # 字符累加 x 对…取模 2
        x = x // 2  # 把 x 除以 除以 2 存入 x
    return c  # 返回 字符


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(onesCount(1))  # 打印输出
