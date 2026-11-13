# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
# 合并 K 个升序链表 - 方案: 收集所有值 + 排序 + 重建


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def merge_k_lists(lists):  # 定义函数 merge_k_lists（参数：lists）
    vals = []  # 把 [] 存入 vals
    for l in lists:  # 逐个取出 lists 的元素（左指针）
        while l:  # 循环，直到不满足「左指针」
            vals.append(l.val)  # 把 左指针.值 追加到列表尾部
            l = l.next  # 把 左指针.下一个 存入 左指针
    vals.sort()  # 排序
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    for v in vals:  # 逐个取出 vals 的元素（值）
        curr.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def build(arr):  # 定义函数 build（参数：数组）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    for v in arr:  # 逐个取出 数组 的元素（值）
        curr.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def to_list(node):  # 定义函数 to_list（参数：节点）
    res = []  # 把 [] 存入 结果
    while node:  # 循环，直到不满足「节点」
        res.append(node.val)  # 把 节点.值 追加到列表尾部
        node = node.next  # 把 节点.下一个 存入 节点
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    print(to_list(merge_k_lists(lists)))  # [1, 1, 2, 3, 4, 4, 5, 6]
