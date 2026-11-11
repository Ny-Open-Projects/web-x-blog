# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134358253
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def mergeTwoLists(list1, list2):  # 定义函数 mergeTwoLists（参数：list1, list2）
    if not list1:  # 若 not list1
        return list2  # 返回 list2
    if not list2:  # 若 not list2
        return list1  # 返回 list1
    if list1.val < list2.val:  # 若 list1.值 小于 list2.值
        list1.next = mergeTwoLists(list1.next, list2)  # 把 mergeTwoLists(list1.下一个, list2) 写入 下一个
        return list1  # 返回 list1
    else:  # 否则
        list2.next = mergeTwoLists(list1, list2.next)  # 把 mergeTwoLists(list1, list2.下一个) 写入 下一个
        return list2  # 返回 list2


def build(arr):  # 定义函数 build（参数：数组）
    dummy = ListNode()  # 把 ListNode() 存入 哨兵节点
    cur = dummy  # 把 哨兵节点 存入 当前值
    for v in arr:  # 逐个取出 数组 的元素（值）
        cur.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
        cur = cur.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def to_list(node):  # 定义函数 to_list（参数：节点）
    out = []  # 把 [] 存入 out
    while node:  # 循环，直到不满足「节点」
        out.append(node.val)  # 把 节点.值 追加到列表尾部
        node = node.next  # 把 节点.下一个 存入 节点
    return out  # 返回 out


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    l1 = build([1, 2, 4])  # 把 build([1, 2, 4]) 存入 l1
    l2 = build([1, 3, 4])  # 把 build([1, 3, 4]) 存入 l2
    print(to_list(mergeTwoLists(l1, l2)))  # 打印输出
