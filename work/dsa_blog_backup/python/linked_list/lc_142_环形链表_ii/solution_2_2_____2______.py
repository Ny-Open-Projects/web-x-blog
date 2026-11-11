# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094299
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def detectCycle(head):  # 定义函数 detectCycle（参数：头节点）
    if not head:  # 若 not 头节点
        return None  # 返回 None
    slow = fast = head  # 把 快指针 赋值为 头节点 存入 慢指针
    while fast:  # 循环，直到不满足「快指针」
        slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        if not fast.next:  # 若 not 快指针.下一个
            return None  # 返回 None
        fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
        if fast == slow:  # 若 快指针 等于 慢指针
            ptr = head  # 把 头节点 存入 ptr
            while ptr != slow:  # 循环，直到不满足「ptr 不等于 慢指针」
                ptr = ptr.next  # 把 ptr.下一个 存入 ptr
                slow = slow.next  # 把 慢指针.下一个 存入 慢指针
            return ptr  # 返回 ptr
    return None  # 返回 None


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(detectCycle(None))  # 打印输出
