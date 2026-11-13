# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134358253
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def mergeTwoLists(list1, list2):  # 定义函数 mergeTwoLists（参数：list1, list2）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    p = dummy  # 把 哨兵节点 存入 节点
    p1, p2 = list1, list2  # 把 list1, list2 写入 p1, p2
    while p1 and p2:  # 循环，直到不满足「p1 and p2」
        if p1.val < p2.val:  # 若 p1.值 小于 p2.值
            p.next = p1  # 把 p1 写入 下一个
            p1 = p1.next  # 把 p1.下一个 存入 p1
        else:  # 否则
            p.next = p2  # 把 p2 写入 下一个
            p2 = p2.next  # 把 p2.下一个 存入 p2
        p = p.next  # 把 节点.下一个 存入 节点
    if p1:  # 若 p1
        p.next = p1  # 把 p1 写入 下一个
    if p2:  # 若 p2
        p.next = p2  # 把 p2 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'

    def build(vals):  # 定义函数 build（参数：vals）
        dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
        p = dummy  # 把 哨兵节点 存入 节点
        for v in vals:  # 逐个取出 vals 的元素（值）
            p.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
            p = p.next  # 把 节点.下一个 存入 节点
        return dummy.next  # 返回 哨兵节点.下一个

    list1 = build([1, 2, 4])  # 把 build([1, 2, 4]) 存入 list1
    list2 = build([1, 3, 4])  # 把 build([1, 3, 4]) 存入 list2
    merged = mergeTwoLists(list1, list2)  # 把 mergeTwoLists(list1, list2) 存入 merged
    res = []  # 把 [] 存入 结果
    while merged:  # 循环，直到不满足「merged」
        res.append(merged.val)  # 把 merged.值 追加到列表尾部
        merged = merged.next  # 把 merged.下一个 存入 merged
    print(res)  # [1, 1, 2, 3, 4, 4]
