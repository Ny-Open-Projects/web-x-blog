# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
# 合并 K 个升序链表 - 方案: 分治合并 (自顶向下, 两两合并)


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
    if not lists:  # 若 not lists
        return None  # 返回 None

    def divide(lo, hi):  # 定义函数 divide（参数：左边界, 右边界）
        if lo == hi:  # 若 左边界 等于 右边界
            return lists[lo]  # 返回 lists[左边界]
        mid = (lo + hi) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 中点
        left = divide(lo, mid)  # 把 divide(左边界, 中点) 存入 左边界
        right = divide(mid + 1, hi)  # 把 divide(中点 加 1, 右边界) 存入 右边界
        return merge_two(left, right)  # 返回 merge_two(左边界, 右边界)

    return divide(0, len(lists) - 1)  # 返回 divide(0, 长度(lists) 减 1)


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
