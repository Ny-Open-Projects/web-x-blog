# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095015
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getIntersectionNode(headA, headB):  # 定义函数 getIntersectionNode（参数：链表 A, 链表 B）
    visited = set()  # 把 set() 存入 已访问集合
    temp = headA  # 把 链表 A 存入 临时变量
    while temp:  # 循环，直到不满足「临时变量」
        visited.add(temp)  # 已访问集合 追加 临时变量)
        temp = temp.next  # 把 临时变量.下一个 存入 临时变量
    temp = headB  # 把 链表 B 存入 临时变量
    while temp:  # 循环，直到不满足「临时变量」
        if temp in visited:  # 若 临时变量 in 已访问集合
            return temp  # 返回 临时变量
        temp = temp.next  # 把 临时变量.下一个 存入 临时变量
    return None  # 返回 None


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getIntersectionNode(None, None))  # 打印输出
