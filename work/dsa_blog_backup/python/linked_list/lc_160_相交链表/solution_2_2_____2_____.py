# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095015
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getIntersectionNode(headA, headB):  # 定义函数 getIntersectionNode（参数：链表 A, 链表 B）
    if not headA or not headB:  # 若 not 链表 A or not 链表 B
        return None  # 返回 None
    pA, pB = headA, headB  # 把 链表 A, 链表 B 写入 pA, pB
    while pA != pB:  # 循环，直到不满足「pA 不等于 pB」
        pA = pB if pA is None else pA.next  # 把 pB if pA is None else pA.下一个 存入 pA
        pB = pA if pB is None else pB.next  # 把 pA if pB is None else pB.下一个 存入 pB
    return pA  # 返回 pA


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getIntersectionNode(None, None))  # 打印输出
