# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasCycle(head):  # 定义函数 hasCycle（参数：头节点）
    cursor = head  # 把 头节点 存入 cursor
    visited = {}  # 把 {} 存入 已访问集合
    while cursor:  # 循环，直到不满足「cursor」
        if cursor in visited:  # 若 cursor in 已访问集合
            return True  # 返回 True
        visited[cursor] = True  # 把 True 写入 visited[cursor]
        cursor = cursor.next  # 把 cursor.下一个 存入 cursor
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasCycle(None))  # 打印输出
