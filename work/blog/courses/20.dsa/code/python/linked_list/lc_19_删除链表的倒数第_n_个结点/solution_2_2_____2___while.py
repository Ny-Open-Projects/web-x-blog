# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145093774
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


def removeNthFromEnd(head, n):  # 定义函数 removeNthFromEnd（参数：头节点, 元素个数）
    dummy = ListNode(0, head)  # 把 ListNode(0, 头节点) 存入 哨兵节点
    slow = dummy  # 把 哨兵节点 存入 慢指针
    fast = dummy  # 把 哨兵节点 存入 快指针
    for _ in range(n):  # 让 _ 从 元素个数 遍历
        fast = fast.next  # 把 快指针.下一个 存入 快指针
    while fast.next:  # 循环，直到不满足「快指针.下一个」
        fast = fast.next  # 把 快指针.下一个 存入 快指针
        slow = slow.next  # 把 慢指针.下一个 存入 慢指针
    slow.next = slow.next.next  # 把 慢指针.下一个.下一个 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    head = build_list([1, 2, 3, 4, 5])  # 把 build_list([1, 2, 3, 4, 5]) 存入 头节点
    head = removeNthFromEnd(head, 2)  # 把 removeNthFromEnd(头节点, 2) 存入 头节点
    print(list_to_arr(head))  # 打印输出
