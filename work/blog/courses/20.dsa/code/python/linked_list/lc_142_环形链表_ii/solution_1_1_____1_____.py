# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094299
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def detectCycle(head):  # 定义函数 detectCycle（参数：头节点）
    visited = set()  # 把 set() 存入 已访问集合
    while head:  # 循环，直到不满足「头节点」
        if head in visited:  # 若 头节点 in 已访问集合
            return head  # 返回 头节点
        visited.add(head)  # 已访问集合 追加 头节点)
        head = head.next  # 把 头节点.下一个 存入 头节点
    return None  # 返回 None


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(detectCycle(None))  # 打印输出
