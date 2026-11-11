# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130514894
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, x):  # 构造函数：初始化成员
        self.val = x  # 把 x 写入 值
        self.next = None  # 把 None 写入 下一个


def hasCycle(head):  # 定义函数 hasCycle（参数：头节点）
    # 引入虚拟头节点，统一处理空链表与首节点即入环的情况
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    dummy.next = head  # 把 头节点 写入 下一个
    slow = fast = dummy  # 把 快指针 赋值为 哨兵节点 存入 慢指针
    while fast and fast.next:  # 循环，直到不满足「快指针 and 快指针.下一个」
        slow = slow.next  # 把 慢指针.下一个 存入 慢指针
        fast = fast.next.next  # 把 快指针.下一个.下一个 存入 快指针
        if slow == fast:  # 若 慢指针 等于 快指针
            return True  # 返回 True
    return False  # 返回 False


def build(vals, pos):  # 定义函数 build（参数：vals, pos）
    nodes = [ListNode(v) for v in vals]  # 把 [ListNode(值) for 值 in vals] 存入 nodes
    for i in range(len(nodes) - 1):  # 让 下标 i 从 长度(nodes 遍历
        nodes[i].next = nodes[i + 1]  # 把 nodes[下标 i 加 1] 写入 下一个
    if pos >= 0 and nodes:  # 若 pos 不低于 0 and nodes
        nodes[-1].next = nodes[pos]  # 把 nodes[pos] 写入 下一个
    return nodes[0] if nodes else None  # 返回 nodes[0] if nodes else None


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(hasCycle(build([3, 2, 0, -4], 1)))  # 打印输出
    print(hasCycle(build([1, 2], 0)))  # 打印输出
    print(hasCycle(build([1], -1)))  # 打印输出
    print(hasCycle(None))  # 打印输出
