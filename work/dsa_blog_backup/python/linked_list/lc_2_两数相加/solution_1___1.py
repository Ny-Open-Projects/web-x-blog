# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
# Definition for singly-linked list.
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def build_list(vals):  # 定义函数 build_list（参数：vals）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    for v in vals:  # 逐个取出 vals 的元素（值）
        curr.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def print_list(head):  # 定义函数 print_list（参数：头节点）
    res = []  # 把 [] 存入 结果
    while head:  # 循环，直到不满足「头节点」
        res.append(str(head.val))  # 把 str(头节点.值 追加到列表尾部
        head = head.next  # 把 头节点.下一个 存入 头节点
    return "->".join(res)  # 返回 ' 减 超过 '.join(结果)


def addTwoNumbers(l1, l2):  # 定义函数 addTwoNumbers（参数：l1, l2）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    carry = 0  # 把 0 存入 carry
    while l1 or l2:  # 循环，直到不满足「l1 or l2」
        v1 = l1.val if l1 else 0  # 把 l1.值 if l1 else 0 存入 v1
        v2 = l2.val if l2 else 0  # 把 l2.值 if l2 else 0 存入 v2
        total = v1 + v2 + carry  # 把 v1 加 v2 加 carry 存入 总和
        carry = total // 10  # 把 总和 除以 除以 10 存入 carry
        curr.next = ListNode(total % 10)  # 把 ListNode(总和 对…取模 10) 写入 下一个
        curr = curr.next  # 把 当前值.下一个 存入 当前值
        l1 = l1.next if l1 else None  # 把 l1.下一个 if l1 else None 存入 l1
        l2 = l2.next if l2 else None  # 把 l2.下一个 if l2 else None 存入 l2
    if carry:  # 若 carry
        curr.next = ListNode(carry)  # 把 ListNode(carry) 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    l1 = build_list([2, 4, 3])  # 把 build_list([2, 4, 3]) 存入 l1
    l2 = build_list([5, 6, 4])  # 把 build_list([5, 6, 4]) 存入 l2
    result = addTwoNumbers(l1, l2)  # 把 addTwoNumbers(l1, l2) 存入 结果
    print(print_list(result))  # 打印输出
