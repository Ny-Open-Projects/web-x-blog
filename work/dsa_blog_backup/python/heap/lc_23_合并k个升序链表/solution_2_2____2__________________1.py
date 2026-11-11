# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


class Status:  # 定义类
    def __init__(self, val, ptr):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.ptr = ptr  # 把 ptr 写入 self.ptr

    def __lt__(self, other):  # 定义函数 __lt__（参数：self, other）
        return self.val < other.val  # 返回 self.值 小于 other.值


class PQ:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    @property  # @property
    def length(self):  # 定义函数 length（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)

    def push(self, item):  # 定义函数 push（参数：self, item）
        heapq.heappush(self.heap, item)  # heapq.heappush(self.堆, item)

    def pop(self):  # 定义函数 pop（参数：self）
        return heapq.heappop(self.heap)  # 返回 heapq.heappop(self.堆)


def mergeKLists(lists):  # 定义函数 mergeKLists（参数：lists）
    queue = PQ()  # 把 PQ() 存入 队列
    for node in lists:  # 逐个取出 lists 的元素（节点）
        if node is not None:  # 若 节点 is not None
            queue.push(Status(node.val, node))  # 把 Status(节点.值, 节点 压入栈/数组尾部
    head = ListNode(0)  # 把 ListNode(0) 存入 头节点
    tail = head  # 把 头节点 存入 尾节点
    while queue.length > 0:  # 循环，直到不满足「队列.长度 超过 0」
        f = queue.pop()  # 把 队列 弹出 ) 存入 f
        if f:  # 若 f
            tail.next = f.ptr  # 把 f.ptr 写入 下一个
            tail = tail.next  # 把 尾节点.下一个 存入 尾节点
            if f.ptr.next is not None:  # 若 f.ptr.下一个 is not None
                queue.push(
                    Status(f.ptr.next.val, f.ptr.next)
                )  # 把 Status(f.ptr.下一个.值, f.ptr.下一个 压入栈/数组尾部
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
