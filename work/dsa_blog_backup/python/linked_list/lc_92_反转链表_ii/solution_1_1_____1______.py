# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseLinkedList(head):  # 定义函数 reverseLinkedList（参数：头节点）
    prev = None  # 把 None 存入 前一个
    curr = head  # 把 头节点 存入 当前值
    while curr:  # 循环，直到不满足「当前值」
        nxt = curr.next  # 把 当前值.下一个 存入 nxt
        curr.next = prev  # 把 前一个 写入 下一个
        prev = curr  # 把 当前值 存入 前一个
        curr = nxt  # 把 nxt 存入 当前值
    return prev  # 返回 前一个


def reverseBetween(head, left, right):  # 定义函数 reverseBetween（参数：头节点, 左边界, 右边界）
    dummy = ListNode(-1)  # 把 ListNode( 减 1) 存入 哨兵节点
    dummy.next = head  # 把 头节点 写入 下一个
    pre = dummy  # 把 哨兵节点 存入 前缀和
    for _ in range(left - 1):  # 让 _ 从 左边界 减 1 遍历
        pre = pre.next  # 把 前缀和.下一个 存入 前缀和
    left_node = pre.next  # 把 前缀和.下一个 存入 left_node
    right_node = pre  # 把 前缀和 存入 right_node
    for _ in range(right - left):  # 让 _ 从 右边界 减 左边界 遍历
        right_node = right_node.next  # 把 right_node.下一个 存入 right_node
    curr = right_node.next  # 把 right_node.下一个 存入 当前值
    pre.next = None  # 把 None 写入 下一个
    right_node.next = None  # 把 None 写入 下一个
    reverseLinkedList(left_node)  # reverseLinkedList(left_node)
    pre.next = right_node  # 把 right_node 写入 下一个
    left_node.next = curr  # 把 当前值 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseLinkedList(None))  # 打印输出
