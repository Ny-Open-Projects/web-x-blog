# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def mergeKLists(lists):  # 定义函数 mergeKLists（参数：lists）
    return merge(lists, 0, len(lists) - 1)  # 返回 merge(lists, 0, 长度(lists) 减 1)


def merge(lists, l, r):  # 定义函数 merge（参数：lists, 左指针, 右指针）
    if l == r:  # 若 左指针 等于 右指针
        return lists[l]  # 返回 lists[左指针]
    if l > r:  # 若 左指针 超过 右指针
        return None  # 返回 None
    mid = (l + r) // 2  # 把 (左指针 加 右指针) 除以 除以 2 存入 中点
    return mergeTwoLists(merge(lists, l, mid), merge(lists, mid + 1, r))


def mergeTwoLists(a, b):  # 定义函数 mergeTwoLists（参数：数组, b）
    if a is None:  # 若 数组 is None
        return b  # 返回 b
    if b is None:  # 若 b is None
        return a  # 返回 数组
    head = ListNode(0)  # 把 ListNode(0) 存入 头节点
    tail = head  # 把 头节点 存入 尾节点
    aPtr = a  # 把 数组 存入 aPtr
    bPtr = b  # 把 b 存入 bPtr
    while aPtr is not None and bPtr is not None:  # 循环，直到不满足「aPtr is not None and bPtr is not None」
        if aPtr.val < bPtr.val:  # 若 aPtr.值 小于 bPtr.值
            tail.next = aPtr  # 把 aPtr 写入 下一个
            aPtr = aPtr.next  # 把 aPtr.下一个 存入 aPtr
        else:  # 否则
            tail.next = bPtr  # 把 bPtr 写入 下一个
            bPtr = bPtr.next  # 把 bPtr.下一个 存入 bPtr
        tail = tail.next  # 把 尾节点.下一个 存入 尾节点
    tail.next = aPtr if aPtr is not None else bPtr  # 把 aPtr if aPtr is not None else bPtr 写入 下一个
    return head.next  # 返回 头节点.下一个


def build(vals):  # 定义函数 build（参数：vals）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    cur = dummy  # 把 哨兵节点 存入 当前值
    for v in vals:  # 逐个取出 vals 的元素（值）
        cur.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
        cur = cur.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def to_list(node):  # 定义函数 to_list（参数：节点）
    res = []  # 把 [] 存入 结果
    while node:  # 循环，直到不满足「节点」
        res.append(node.val)  # 把 节点.值 追加到列表尾部
        node = node.next  # 把 节点.下一个 存入 节点
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]  # 把 [[1, 4, 5], [1, 3, 4], [2, 6]] 存入 lists
    built = [build(l) for l in lists]  # 把 [build(左指针) for 左指针 in lists] 存入 built
    print(to_list(mergeKLists(built)))  # 打印输出
