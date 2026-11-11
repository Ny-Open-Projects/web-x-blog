# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134625776
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def invertTree(root):  # 定义函数 invertTree（参数：根节点）
    if not root:  # 若 not 根节点
        return None  # 返回 None
    q = deque([root])  # 把 deque([根节点]) 存入 节点
    while q:  # 循环，直到不满足「节点」
        node = q.popleft()  # 把 节点.popleft() 存入 节点
        node.left, node.right = node.right, node.left  # 把 节点.右边界, 节点.左边界 写入 右边界
        if node.left:  # 若 节点.左边界
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
        if node.right:  # 若 节点.右边界
            q.append(node.right)  # 把 节点.右边界 追加到列表尾部
    return root  # 返回 根节点


def build_tree(vals):  # 定义函数 build_tree（参数：vals）
    if not vals:  # 若 not vals
        return None  # 返回 None
    root = TreeNode(vals[0])  # 把 TreeNode(vals[0]) 存入 根节点
    q = [root]  # 把 [根节点] 存入 节点
    i = 1  # 把 1 存入 下标 i
    while i < len(vals):  # 循环，直到不满足「下标 i 小于 长度(vals」
        node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
        if vals[i] is not None:  # 若 vals[下标 i] is not None
            node.left = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 左边界
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
        i += 1  # 下标 i累加 1
        if i < len(vals):  # 若 下标 i 小于 长度(vals
            if vals[i] is not None:  # 若 vals[下标 i] is not None
                node.right = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 右边界
                q.append(node.right)  # 把 节点.右边界 追加到列表尾部
            i += 1  # 下标 i累加 1
    return root  # 返回 根节点


def to_list(root):  # 定义函数 to_list（参数：根节点）
    if not root:  # 若 not 根节点
        return []  # 返回 []
    res, q = [], [root]  # 把 [], [根节点] 写入 res, q
    while q:  # 循环，直到不满足「节点」
        node = q.pop(0)  # 把 节点 弹出 0) 存入 节点
        if node:  # 若 节点
            res.append(node.val)  # 把 节点.值 追加到列表尾部
            q.append(node.left)  # 把 节点.左边界 追加到列表尾部
            q.append(node.right)  # 把 节点.右边界 追加到列表尾部
        else:  # 否则
            res.append(None)  # 把 None 追加到列表尾部
    while res and res[-1] is None:  # 循环，直到不满足「结果 and 结果[ 减 1] is None」
        res.pop()  # 弹出栈顶元素
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = build_tree([4, 2, 7, 1, 3, 6, 9])  # 把 build_tree([4, 2, 7, 1, 3, 6, 9]) 存入 根节点
    print(to_list(invertTree(root)))  # 打印输出
