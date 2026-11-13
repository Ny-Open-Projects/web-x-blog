# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasCycle(head):  # 定义函数 hasCycle（参数：头节点）
    if not head:  # 若 not 头节点
        return False  # 返回 False
    slow = head  # 把 头节点 存入 慢指针
    fast = head.next  # 把 头节点.下一个 存入 快指针
    while fast and fast.next:  # 循环，直到不满足「快指针 and 快指针.下一个」
        if slow == fast:  # 若 慢指针 等于 快指针
            return True  # 返回 True
        slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasCycle(None))  # 打印输出
