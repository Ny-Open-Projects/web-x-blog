# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386298
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
        return None  # 返回 None
    from collections import deque  # from collections import deque

    queue = deque([root])  # 把 deque([根节点]) 存入 队列
    while queue:  # 循环，直到不满足「队列」
        n = len(queue)  # 把 长度(队列) 存入 元素个数
        prev = None  # 把 None 存入 前一个
        for _ in range(n):  # 让 _ 从 元素个数 遍历
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
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))  # Node(3, None, Node(7)))
    connect(root)  # connect(根节点)
    print("level1 next:", root.left.next.val if root.left.next else None)  # 打印输出
    print(
        "level2 chain:", root.left.left.next.val, root.left.left.next.next.val
    )  # 根节点.左边界.左边界.下一个.下一个.值)
