# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseList(head):  # 定义函数 reverseList（参数：头节点）
    if not head or not head.next:  # 若 not 头节点 or not 头节点.下一个
        return head  # 返回 头节点
    new_head = reverseList(head.next)  # 把 reverseList(头节点.下一个) 存入 new_head
    head.next.next = head  # 把 头节点 写入 下一个
    head.next = None  # 把 None 写入 下一个
    return new_head  # 返回 new_head


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseList(None))  # 打印输出
