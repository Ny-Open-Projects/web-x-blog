# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130508569
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def deleteNode(node):  # 定义函数 deleteNode（参数：节点）
    curr = node  # 把 节点 存入 当前值
    while curr and curr.next:  # 循环，直到不满足「当前值 and 当前值.下一个」
        curr.val = curr.next.val  # 把 当前值.下一个.值 写入 值
        if not curr.next.next:  # 若 not 当前值.下一个.下一个
            curr.next = None  # 把 None 写入 下一个
            break  # 跳出循环
        curr = curr.next  # 把 当前值.下一个 存入 当前值


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(deleteNode(None))  # 打印输出
