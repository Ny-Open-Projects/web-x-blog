# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095646
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


def removeElements(head, val):  # 定义函数 removeElements（参数：头节点, 值）
    dummy = ListNode(0, head)  # 把 ListNode(0, 头节点) 存入 哨兵节点
    temp = dummy  # 把 哨兵节点 存入 临时变量
    while temp.next:  # 循环，直到不满足「临时变量.下一个」
        if temp.next.val == val:  # 若 临时变量.下一个.值 等于 值
            temp.next = temp.next.next  # 把 临时变量.下一个.下一个 写入 下一个
        else:  # 否则
            temp = temp.next  # 把 临时变量.下一个 存入 临时变量
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    head = build_list([1, 2, 6, 3, 4, 5, 6])  # 把 build_list([1, 2, 6, 3, 4, 5, 6]) 存入 头节点
    result = removeElements(head, 6)  # 把 removeElements(头节点, 6) 存入 结果
    print(print_list(result))  # 打印输出
