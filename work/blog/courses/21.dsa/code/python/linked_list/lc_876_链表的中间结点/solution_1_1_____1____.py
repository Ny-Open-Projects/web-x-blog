# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096505
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class ListNode:  # 定义类
    def __init__(self, val=0, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.next = next  # 把 下一个 写入 下一个


def middleNode(head):  # 定义函数 middleNode（参数：头节点）
    arr = [head]  # 把 [头节点] 存入 数组
    while arr[-1].next:  # 循环，直到不满足「数组[ 减 1].下一个」
        arr.append(arr[-1].next)  # 把 数组[ 减 1].下一个 追加到列表尾部
    return arr[len(arr) // 2]  # 返回 数组[长度(数组) 除以 除以 2]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'

    def build(vals):  # 定义函数 build（参数：vals）
        dummy = ListNode(0)  # 把 ListNode(0) 存入 哨兵节点
        p = dummy  # 把 哨兵节点 存入 节点
        for v in vals:  # 逐个取出 vals 的元素（值）
            p.next = ListNode(v)  # 把 ListNode(值) 写入 下一个
            p = p.next  # 把 节点.下一个 存入 节点
        return dummy.next  # 返回 哨兵节点.下一个

    head = build([1, 2, 3, 4, 5])  # 把 build([1, 2, 3, 4, 5]) 存入 头节点
    mid = middleNode(head)  # 把 middleNode(头节点) 存入 中点
    print(mid.val)  # 3
