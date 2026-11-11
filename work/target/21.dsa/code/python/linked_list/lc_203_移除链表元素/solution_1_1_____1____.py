# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095646
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def removeElements(head, val):  # 定义函数 removeElements（参数：头节点, 值）
    if not head:  # 若 not 头节点
        return None  # 返回 None
    head.next = removeElements(head.next, val)  # 把 removeElements(头节点.下一个, 值) 写入 下一个
    return head.next if head.val == val else head  # 返回 头节点.下一个 if 头节点.值 等于 值 else 头节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(removeElements(None, 1))  # 打印输出
