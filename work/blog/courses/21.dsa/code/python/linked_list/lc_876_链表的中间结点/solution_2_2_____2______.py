# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096505
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def middleNode(head):  # 定义函数 middleNode（参数：头节点）
    n = 0  # 把 0 存入 元素个数
    cur = head  # 把 头节点 存入 当前值
    while cur:  # 循环，直到不满足「当前值」
        ++n  # 加一 元素个数
        cur = cur.next  # 把 当前值.下一个 存入 当前值
    k = 0  # 把 0 存入 下标 k
    cur = head  # 把 头节点 存入 当前值
    while k < int(n / 2):  # 循环，直到不满足「下标 k 小于 int(元素个数 除以 2」
        ++k  # 加一 下标 k
        cur = cur.next  # 把 当前值.下一个 存入 当前值
    return cur  # 返回 当前值


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(middleNode(None))  # 打印输出
