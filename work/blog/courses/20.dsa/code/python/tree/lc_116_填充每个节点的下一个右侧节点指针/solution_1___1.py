# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386215
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    def __init__(self, val=0, left=None, right=None, next=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界
        self.next = next  # 把 下一个 写入 下一个


def connect(root):  # 定义函数 connect（参数：根节点）
    if not root:  # 若 not 根节点
        return root  # 返回 根节点
    from collections import deque  # from collections import deque

    queue = deque([root])  # 把 deque([根节点]) 存入 队列
    while queue:  # 循环，直到不满足「队列」
        level_size = len(queue)  # 把 长度(队列) 存入 level_size
        prev = None  # 把 None 存入 前一个
        for i in range(level_size):  # 让 下标 i 从 level_size 遍历
            node = queue.popleft()  # 把 队列.popleft() 存入 节点
            if prev:  # 若 前一个
                prev.next = node  # 把 节点 写入 下一个
            prev = node  # 把 节点 存入 前一个
            if node.left:  # 若 节点.左边界
                queue.append(node.left)  # 把 节点.左边界 追加到列表尾部
            if node.right:  # 若 节点.右边界
                queue.append(node.right)  # 把 节点.右边界 追加到列表尾部
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build perfect binary tree: [1,2,3,4,5,6,7]
    root = Node(1)  # 把 Node(1) 存入 根节点
    root.left = Node(2)  # 把 Node(2) 写入 左边界
    root.right = Node(3)  # 把 Node(3) 写入 右边界
    root.left.left = Node(4)  # 把 Node(4) 写入 左边界
    root.left.right = Node(5)  # 把 Node(5) 写入 右边界
    root.right.left = Node(6)  # 把 Node(6) 写入 左边界
    root.right.right = Node(7)  # 把 Node(7) 写入 右边界
    connect(root)  # connect(根节点)
    # print each level joined by "->"
    cur = root  # 把 根节点 存入 当前值
    while cur:  # 循环，直到不满足「当前值」
        vals = []  # 把 [] 存入 vals
        node = cur  # 把 当前值 存入 节点
        while node:  # 循环，直到不满足「节点」
            vals.append(str(node.val))  # 把 str(节点.值 追加到列表尾部
            node = node.next  # 把 节点.下一个 存入 节点
        print("->".join(vals))  # 打印输出
        cur = cur.left  # 把 当前值.左边界 存入 当前值
