# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortList(head):  # 定义函数 sortList（参数：头节点）
    nodes = []  # 把 [] 存入 nodes
    curr = head  # 把 头节点 存入 当前值
    while curr:  # 循环，直到不满足「当前值」
        nodes.append(curr)  # 把 当前值 追加到列表尾部
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    nodes.sort(key=lambda x: x.val)  # 排序
    for i in range(len(nodes) - 1):  # 让 下标 i 从 长度(nodes 遍历
        nodes[i].next = nodes[i + 1]  # 把 nodes[下标 i 加 1] 写入 下一个
    if nodes:  # 若 nodes
        nodes[-1].next = None  # 把 None 写入 下一个
    return nodes[0] if nodes else None  # 返回 nodes[0] if nodes else None


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortList(None))  # 打印输出
