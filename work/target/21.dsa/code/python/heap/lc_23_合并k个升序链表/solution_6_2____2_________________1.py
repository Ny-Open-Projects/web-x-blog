# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
# 合并 K 个升序链表 - 方案: 小顶堆 (用 id 做 tiebreak, 避免比较节点)
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def merge_k_lists(lists):  # 定义函数 merge_k_lists（参数：lists）
    heap = []  # 把 [] 存入 堆
    for node in lists:  # 逐个取出 lists 的元素（节点）
        if node:  # 若 节点
            heapq.heappush(heap, (node.val, id(node), node))  # heapq.heappush(堆, (节点.值, id(节点), 节点))
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    curr = dummy  # 把 哨兵节点 存入 当前值
    while heap:  # 循环，直到不满足「堆」
        _, _, node = heapq.heappop(heap)  # 把 heapq.heappop(堆) 写入 _, _, node
        curr.next = node  # 把 节点 写入 下一个
        curr = curr.next  # 把 当前值.下一个 存入 当前值
        if node.next:  # 若 节点.下一个
            heapq.heappush(
                heap, (node.next.val, id(node.next), node.next)
            )  # heapq.heappush(堆, (节点.下一个.值, id(节点.下一个), 节点.下一个))
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
