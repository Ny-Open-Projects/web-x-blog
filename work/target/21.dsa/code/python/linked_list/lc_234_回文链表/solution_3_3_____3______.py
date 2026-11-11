# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def isPalindrome(head):  # 定义函数 isPalindrome（参数：头节点）
    def reverse_list(node):  # 定义函数 reverse_list（参数：节点）
        prev = None  # 把 None 存入 前一个
        curr = node  # 把 节点 存入 当前值
        while curr:  # 循环，直到不满足「当前值」
            nxt = curr.next  # 把 当前值.下一个 存入 nxt
            curr.next = prev  # 把 前一个 写入 下一个
            prev = curr  # 把 当前值 存入 前一个
            curr = nxt  # 把 nxt 存入 当前值
        return prev  # 返回 前一个

    def end_of_first_half(node):  # 定义函数 end_of_first_half（参数：节点）
        fast = slow = node  # 把 慢指针 赋值为 节点 存入 快指针
        while fast.next and fast.next.next:  # 循环，直到不满足「快指针.下一个 and 快指针.下一个.下一个」
            fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
            slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        return slow  # 返回 慢指针

    if not head:  # 若 not 头节点
        return True  # 返回 True
    first_half_end = end_of_first_half(head)  # 把 end_of_first_half(头节点) 存入 first_half_end
    second_half_start = reverse_list(
        first_half_end.next
    )  # 把 reverse_list(first_half_end.下一个) 存入 second_half_start

    p1, p2 = head, second_half_start  # 把 头节点, second_half_start 写入 p1, p2
    result = True  # 把 True 存入 结果
    while p2 and result:  # 循环，直到不满足「p2 and 结果」
        if p1.val != p2.val:  # 若 p1.值 不等于 p2.值
            result = False  # 把 False 存入 结果
        p1 = p1.next  # 把 p1.下一个 存入 p1
        p2 = p2.next  # 把 p2.下一个 存入 p2

    first_half_end.next = reverse_list(second_half_start)  # 把 reverse_list(second_half_start) 写入 下一个
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isPalindrome(None))  # 打印输出
