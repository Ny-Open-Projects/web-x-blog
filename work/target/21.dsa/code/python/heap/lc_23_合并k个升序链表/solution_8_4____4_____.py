# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
# 合并 K 个升序链表 - 方案: 分治合并 (自底向上, 逐对合并)


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def merge_two(a, b):  # 定义函数 merge_two（参数：数组, b）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    while a and b:  # 循环，直到不满足「数组 and b」
        if a.val <= b.val:  # 若 数组.值 不超过 b.值
            curr.next = a  # 把 数组 写入 下一个
            a = a.next  # 把 数组.下一个 存入 数组
        else:  # 否则
            curr.next = b  # 把 b 写入 下一个
            b = b.next  # 把 b.下一个 存入 b
        curr = curr.next  # 把 当前值.下一个 存入 当前值
    curr.next = a or b  # 把 数组 or b 写入 下一个
    return dummy.next  # 返回 哨兵节点.下一个


def merge_k_lists(lists):  # 定义函数 merge_k_lists（参数：lists）
    lists = [l for l in lists if l]  # 把 [左指针 for 左指针 in lists if 左指针] 存入 lists
    if not lists:  # 若 not lists
        return None  # 返回 None
    while len(lists) > 1:  # 循环，直到不满足「长度(lists) 超过 1」
        merged = []  # 把 [] 存入 merged
        for i in range(0, len(lists), 2):  # 让 下标 i 从 0 到 长度(lists 遍历
            a = lists[i]  # 把 lists[下标 i] 存入 数组
            b = (
                lists[i + 1] if i + 1 < len(lists) else None
            )  # 把 lists[下标 i 加 1] if 下标 i 加 1 小于 长度(lists) else None 存入 b
            merged.append(merge_two(a, b))  # 把 merge_two(数组, b 追加到列表尾部
        lists = merged  # 把 merged 存入 lists
    return lists[0]  # 返回 lists[0]


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
