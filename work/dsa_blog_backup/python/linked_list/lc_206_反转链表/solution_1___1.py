# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseList(head):  # 定义函数 reverseList（参数：头节点）
    p1 = head  # 把 头节点 存入 p1
    p2 = None  # 把 None 存入 p2
    while p1:  # 循环，直到不满足「p1」
        tmp = p1.next  # 把 p1.下一个 存入 临时变量
        p1.next = p2  # 把 p2 写入 下一个
        p2 = p1  # 把 p1 存入 p2
        p1 = tmp  # 把 临时变量 存入 p1
    print(p1 and p1.val, p2 and p2.val)  # 打印输出
    return p2  # 返回 p2


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseList(None))  # 打印输出
