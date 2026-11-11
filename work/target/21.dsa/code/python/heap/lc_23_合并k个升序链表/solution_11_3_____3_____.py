# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
# 合并 K 个升序链表 - 方案: 递归逐条合并 (merge(l0, merge(l1, ...)))


import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def merge_two(a, b):  # 定义函数 merge_two（参数：数组, b）
    if not a:  # 若 not 数组
        return b  # 返回 b
    if not b:  # 若 not b
        return a  # 返回 数组
    if a.val <= b.val:  # 若 数组.值 不超过 b.值
        a.next = merge_two(a.next, b)  # 把 merge_two(数组.下一个, b) 写入 下一个
        return a  # 返回 数组
    else:  # 否则
        b.next = merge_two(a, b.next)  # 把 merge_two(数组, b.下一个) 写入 下一个
        return b  # 返回 b


def merge_k_lists(lists):  # 定义函数 merge_k_lists（参数：lists）
    if not lists:  # 若 not lists
        return None  # 返回 None

    def merge_rest(i):  # 定义函数 merge_rest（参数：下标 i）
        if i == len(lists) - 1:  # 若 下标 i 等于 长度(lists) 减 1
            return lists[i]  # 返回 lists[下标 i]
        return merge_two(
            lists[i], merge_rest(i + 1)
        )  # 返回 merge_two(lists[下标 i], merge_rest(下标 i 加 1))

    return merge_rest(0)  # 返回 merge_rest(0)


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
