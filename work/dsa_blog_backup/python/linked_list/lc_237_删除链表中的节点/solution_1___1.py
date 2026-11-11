# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130508569
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def deleteNode(node):  # 定义函数 deleteNode（参数：节点）
    node.val = node.next.val  # 把 节点.下一个.值 写入 值
    node.next = node.next.next  # 把 节点.下一个.下一个 写入 下一个


def build(nums):  # 定义函数 build（参数：数组）
    dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
    cur = dummy  # 把 哨兵节点 存入 当前值
    for n in nums:  # 逐个取出 数组 的元素（元素个数）
        cur.next = ListNode(n)  # 把 ListNode(元素个数) 写入 下一个
        cur = cur.next  # 把 当前值.下一个 存入 当前值
    return dummy.next  # 返回 哨兵节点.下一个


def to_list(head):  # 定义函数 to_list（参数：头节点）
    res = []  # 把 [] 存入 结果
    while head:  # 循环，直到不满足「头节点」
        res.append(head.val)  # 把 头节点.值 追加到列表尾部
        head = head.next  # 把 头节点.下一个 存入 头节点
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    head = build([4, 5, 1, 9])  # 把 build([4, 5, 1, 9]) 存入 头节点
    # 删除值为 5 的节点（leetcode 237 只给定该节点）
    target = head.next  # 把 头节点.下一个 存入 目标值
    deleteNode(target)  # deleteNode(目标值)
    print(to_list(head))  # 打印输出
