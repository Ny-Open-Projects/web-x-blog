# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


class Node:  # 定义类
    def __init__(self, val=0, left=None, right=None, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界
        self.next = next  # 把 下一个 写入 下一个


def connect(root):  # 定义函数 connect（参数：根节点）
    if not root:  # 若 not 根节点
        return root  # 返回 根节点
    q = deque([root])  # 把 deque([根节点]) 存入 节点
    while q:  # 循环，直到不满足「节点」
        size = len(q)  # 把 长度(节点) 存入 大小
        prev = None  # 把 None 存入 前一个
        for _ in range(size):  # 让 _ 从 大小 遍历
            node = q.popleft()  # 把 节点.popleft() 存入 节点
            if prev:  # 若 前一个
                prev.next = node  # 把 节点 写入 下一个
            prev = node  # 把 节点 存入 前一个
            if node.left:  # 若 节点.左边界
                q.append(node.left)  # 把 节点.左边界 追加到列表尾部
            if node.right:  # 若 节点.右边界
                q.append(node.right)  # 把 节点.右边界 追加到列表尾部
    return root  # 返回 根节点


def build_node(vals):  # 定义函数 build_node（参数：vals）
    if not vals:  # 若 not vals
        return None  # 返回 None
    root = Node(vals[0])  # 把 Node(vals[0]) 存入 根节点
    q = [root]  # 把 [根节点] 存入 节点
    i = 1  # 把 1 存入 下标 i
    while i < len(vals) and q:  # 循环，直到不满足「下标 i 小于 长度(vals) and 节点」
        node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.left = Node(vals[i])  # 把 Node(vals[下标 i]) 写入 左边界
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
        i += 1  # 下标 i累加 1
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.right = Node(vals[i])  # 把 Node(vals[下标 i]) 写入 右边界
            q.append(node.right)  # 把 节点.右边界 追加到列表尾部
        i += 1  # 下标 i累加 1
    return root  # 返回 根节点


def level_vals(node):  # 定义函数 level_vals（参数：节点）
    res = []  # 把 [] 存入 结果
    while node:  # 循环，直到不满足「节点」
        res.append(node.val)  # 把 节点.值 追加到列表尾部
        node = node.next  # 把 节点.下一个 存入 节点
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = build_node([1, 2, 3, 4, 5, None, 7])  # 把 build_node([1, 2, 3, 4, 5, None, 7]) 存入 根节点
    connect(root)  # connect(根节点)
    print(level_vals(root))  # 打印输出
    print(level_vals(root.left))  # 打印输出
