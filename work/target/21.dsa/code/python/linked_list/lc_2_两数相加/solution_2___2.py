# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def addTwoNumbers(l1, l2):  # 定义函数 addTwoNumbers（参数：l1, l2）
    if not l1 and not l2:  # 若 not l1 and not l2
        return None  # 返回 None
    if not l1:  # 若 not l1
        return l2  # 返回 l2
    if not l2:  # 若 not l2
        return l1  # 返回 l1
    head = tail = None  # 把 尾节点 赋值为 None 存入 头节点
    carry = 0  # 把 0 存入 carry
    while l1 or l2:  # 循环，直到不满足「l1 or l2」
        v1 = l1.val if l1 else 0  # 把 l1.值 if l1 else 0 存入 v1
        v2 = l2.val if l2 else 0  # 把 l2.值 if l2 else 0 存入 v2
        total = v1 + v2 + carry  # 把 v1 加 v2 加 carry 存入 总和
        node = ListNode(total % 10)  # 把 ListNode(总和 对…取模 10) 存入 节点
        carry = total // 10  # 把 总和 除以 除以 10 存入 carry
        if not head:  # 若 not 头节点
            head = tail = node  # 把 尾节点 赋值为 节点 存入 头节点
        else:  # 否则
            tail.next = node  # 把 节点 写入 下一个
            tail = node  # 把 节点 存入 尾节点
        l1 = l1.next if l1 else None  # 把 l1.下一个 if l1 else None 存入 l1
        l2 = l2.next if l2 else None  # 把 l2.下一个 if l2 else None 存入 l2
    if carry:  # 若 carry
        tail.next = ListNode(carry)  # 把 ListNode(carry) 写入 下一个
    return head  # 返回 头节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(addTwoNumbers(None, None))  # 打印输出
