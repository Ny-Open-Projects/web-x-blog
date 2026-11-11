# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isPalindrome(head):  # 定义函数 isPalindrome（参数：头节点）
    vals = []  # 把 [] 存入 vals
    while head:  # 循环，直到不满足「头节点」
        vals.append(head.val)  # 把 头节点.值 追加到列表尾部
        head = head.next  # 把 头节点.下一个 存入 头节点
    left, right = 0, len(vals) - 1  # 把 0, 长度(vals) 减 1 写入 left, right
    while left < right:  # 循环，直到不满足「左边界 小于 右边界」
        if vals[left] != vals[right]:  # 若 vals[左边界] 不等于 vals[右边界]
            return False  # 返回 False
        left += 1  # 左边界累加 1
        right -= 1  # 右边界累减 1
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isPalindrome(None))  # 打印输出
