# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513986
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def deleteDuplicates(head):  # 定义函数 deleteDuplicates（参数：头节点）
    if not head:  # 若 not 头节点
        return None  # 返回 None
    if head.next and head.val == head.next.val:  # 若 头节点.下一个 and 头节点.值 等于 头节点.下一个.值
        head.next = head.next.next  # 跳过重复的下一个节点，保留一个副本
        return deleteDuplicates(head)  # 返回 deleteDuplicates(头节点)
    head.next = deleteDuplicates(head.next)  # 把 deleteDuplicates(头节点.下一个) 写入 下一个
    return head  # 返回 头节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(deleteDuplicates(None))  # 打印输出
