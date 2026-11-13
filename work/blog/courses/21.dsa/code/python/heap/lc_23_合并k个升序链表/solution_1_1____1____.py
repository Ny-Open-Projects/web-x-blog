# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


class MinHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def size(self):  # 定义函数 size（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def insert(self, val, node):  # 定义函数 insert（参数：self, 值, 节点）
        heapq.heappush(self.heap, (val, id(node), node))  # heapq.heappush(self.堆, (值, id(节点), 节点))

    def pop(self):  # 定义函数 pop（参数：self）
        val, _id, node = heapq.heappop(self.heap)  # 把 heapq.heappop(self.堆) 写入 val, _id, node
        return node  # 返回 节点


def mergeKLists(lists):  # 定义函数 mergeKLists（参数：lists）
    res = ListNode(0)  # 把 ListNode(0) 存入 结果
    p = res  # 把 结果 存入 节点
    h = MinHeap()  # 把 MinHeap() 存入 h
    for l in lists:  # 逐个取出 lists 的元素（左指针）
        if l:  # 若 左指针
            h.insert(l.val, l)  # h 插入 左指针.值, 左指针)
    while h.size() > 0:  # 循环，直到不满足「h.大小() 超过 0」
        n = h.pop()  # 把 h 弹出 ) 存入 元素个数
        p.next = n  # 把 元素个数 写入 下一个
        p = p.next  # 把 节点.下一个 存入 节点
        if n.next:  # 若 元素个数.下一个
            h.insert(n.next.val, n.next)  # h 插入 元素个数.下一个.值, 元素个数.下一个)
    return res.next  # 返回 结果.下一个


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
