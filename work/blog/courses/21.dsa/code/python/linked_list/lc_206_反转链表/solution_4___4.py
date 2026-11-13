# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseList(head):  # 定义函数 reverseList（参数：头节点）
    prev = None  # 把 None 存入 前一个
    curr = head  # 把 头节点 存入 当前值
    while curr:  # 循环，直到不满足「当前值」
        nxt = curr.next  # 把 当前值.下一个 存入 nxt
        curr.next = prev  # 把 前一个 写入 下一个
        prev = curr  # 把 当前值 存入 前一个
        curr = nxt  # 把 nxt 存入 当前值
    return prev  # 返回 前一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseList(None))  # 打印输出
