# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    # 数组 DP（另一种写法，预先建表）
    fibs = [0, 1]  # 把 [0, 1] 存入 fibs
    for i in range(2, n + 1):  # 让 下标 i 从 2 到 元素个数 加 1 遍历
        fibs.append(fibs[i - 1] + fibs[i - 2])  # 把 fibs[下标 i 减 1] 加 fibs[下标 i 减 2] 追加到列表尾部
    return fibs[n]  # 返回 fibs[元素个数]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(5))  # 打印输出
