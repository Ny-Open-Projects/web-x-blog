# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513986
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def deleteDuplicates(head):  # 定义函数 deleteDuplicates（参数：头节点）
    curr = head  # 把 头节点 存入 当前值
    while curr:  # 循环，直到不满足「当前值」
        while (
            curr.next and curr.val == curr.next.val
        ):  # 循环，直到不满足「当前值.下一个 and 当前值.值 等于 当前值.下一个.值」
            curr.next = curr.next.next  # 把 当前值.下一个.下一个 写入 下一个
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    return head  # 返回 头节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(deleteDuplicates(None))  # 打印输出
