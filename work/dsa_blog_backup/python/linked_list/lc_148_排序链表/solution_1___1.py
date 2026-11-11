# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortList(head):  # 定义函数 sortList（参数：头节点）
    vals = []  # 把 [] 存入 vals
    curr = head  # 把 头节点 存入 当前值
    while curr:  # 循环，直到不满足「当前值」
        vals.append(curr.val)  # 把 当前值.值 追加到列表尾部
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    vals.sort()  # 排序
    curr = head  # 把 头节点 存入 当前值
    for v in vals:  # 逐个取出 vals 的元素（值）
        curr.val = v  # 把 值 写入 值
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    return head  # 返回 头节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortList(None))  # 打印输出
