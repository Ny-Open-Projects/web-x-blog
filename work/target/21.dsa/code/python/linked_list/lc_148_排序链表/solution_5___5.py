# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortList(head):  # 定义函数 sortList（参数：头节点）
    if not head or not head.next:  # 若 not 头节点 or not 头节点.下一个
        return head  # 返回 头节点
    # Find middle
    slow, fast = head, head.next  # 把 头节点, 头节点.下一个 写入 slow, fast
    while fast and fast.next:  # 循环，直到不满足「快指针 and 快指针.下一个」
        slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
    mid = slow.next  # 把 慢指针.下一个 存入 中点
    slow.next = None  # 把 None 写入 下一个
    # Recursively sort two halves
    left = sortList(head)  # 把 sortList(头节点) 存入 左边界
    right = sortList(mid)  # 把 sortList(中点) 存入 右边界
    # Merge
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    while left and right:  # 循环，直到不满足「左边界 and 右边界」
        if left.val <= right.val:  # 若 左边界.值 不超过 右边界.值
            curr.next = left  # 把 左边界 写入 下一个
            left = left.next  # 把 左边界.下一个 存入 左边界
        else:  # 否则
            curr.next = right  # 把 右边界 写入 下一个
            right = right.next  # 把 右边界.下一个 存入 右边界
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    curr.next = left if left else right  # 把 左边界 if 左边界 else 右边界 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortList(None))  # 打印输出
