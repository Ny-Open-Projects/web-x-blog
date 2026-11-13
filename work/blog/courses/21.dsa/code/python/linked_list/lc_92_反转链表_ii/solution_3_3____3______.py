# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def build_list(vals):  # 定义函数 build_list（参数：vals）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    cur = dummy  # 把 哨兵节点 存入 当前值
    for v in vals:  # 逐个取出 vals 的元素（值）
        cur.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
        cur = cur.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def list_to_arr(head):  # 定义函数 list_to_arr（参数：头节点）
    arr = []  # 把 [] 存入 数组
    while head:  # 循环，直到不满足「头节点」
        arr.append(head.val)  # 把 头节点.值 追加到列表尾部
        head = head.next  # 把 头节点.下一个 存入 头节点
    return arr  # 返回 数组


def reverseBetween(head, left, right):  # 定义函数 reverseBetween（参数：头节点, 左边界, 右边界）
    dummy = ListNode(-1)  # 把 ListNode( 减 1) 存入 哨兵节点
    dummy.next = head  # 把 头节点 写入 下一个
    tmp = dummy  # 把 哨兵节点 存入 临时变量
    for _ in range(left - 1):  # 让 _ 从 左边界 减 1 遍历
        tmp = tmp.next  # 把 临时变量.下一个 存入 临时变量
    prev = tmp.next  # 把 临时变量.下一个 存入 前一个
    cur = prev.next  # 把 前一个.下一个 存入 当前值
    for _ in range(right - left):  # 让 _ 从 右边界 减 左边界 遍历
        nxt = cur.next  # 把 当前值.下一个 存入 nxt
        cur.next = prev  # 把 前一个 写入 下一个
        prev = cur  # 把 当前值 存入 前一个
        cur = nxt  # 把 nxt 存入 当前值
    tmp.next.next = cur  # 把 当前值 写入 下一个
    tmp.next = prev  # 把 前一个 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    head = build_list([1, 2, 3, 4, 5])  # 把 build_list([1, 2, 3, 4, 5]) 存入 头节点
    head = reverseBetween(head, 2, 4)  # 把 reverseBetween(头节点, 2, 4) 存入 头节点
    print(list_to_arr(head))  # 打印输出
