# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isPalindrome(head):  # 定义函数 isPalindrome（参数：头节点）
    front_pointer = head  # 把 头节点 存入 front_pointer

    def recursively_check(node):  # 定义函数 recursively_check（参数：节点）
        nonlocal front_pointer  # nonlocal front_pointer
        if node:  # 若 节点
            if not recursively_check(node.next):  # 若 not recursively_check(节点.下一个
                return False  # 返回 False
            if node.val != front_pointer.val:  # 若 节点.值 不等于 front_pointer.值
                return False  # 返回 False
            front_pointer = front_pointer.next  # 把 front_pointer.下一个 存入 front_pointer
        return True  # 返回 True

    return recursively_check(head)  # 返回 recursively_check(头节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isPalindrome(None))  # 打印输出
