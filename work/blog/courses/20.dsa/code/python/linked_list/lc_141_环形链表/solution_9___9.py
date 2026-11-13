# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def hasCycle(head):  # 定义函数 hasCycle（参数：头节点）
    visited = set()  # 把 set() 存入 已访问集合

    def dfs(node):  # 定义函数 dfs（参数：节点）
        if not node:  # 若 not 节点
            return False  # 返回 False
        if node in visited:  # 若 节点 in 已访问集合
            return True  # 返回 True
        visited.add(node)  # 已访问集合 追加 节点)
        return dfs(node.next)  # 返回 dfs(节点.下一个)

    return dfs(head)  # 返回 dfs(头节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasCycle(None))  # 打印输出
