# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130660242
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def fib(n):  # 定义函数 fib（参数：元素个数）
    if n == 0:  # 若 元素个数 等于 0
        return 0  # 返回 0
    if n == 1:  # 若 元素个数 等于 1
        return 1  # 返回 1
    start = 0  # 把 0 存入 起点
    end = 1  # 把 1 存入 终点
    for i in range(2, n + 1):  # 让 下标 i 从 2 到 元素个数 加 1 遍历
        end_tmp = end  # 把 终点 存入 end_tmp
        end = end + start  # 把 终点 加 起点 存入 终点
        start = end_tmp  # 把 end_tmp 存入 起点
    return end  # 返回 终点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(fib(5))  # 打印输出
