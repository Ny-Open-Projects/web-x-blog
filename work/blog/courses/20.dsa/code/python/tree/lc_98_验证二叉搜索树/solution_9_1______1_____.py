# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
from collections import deque  # from collections import deque


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def isValidBST(root):  # 定义函数 isValidBST（参数：根节点）
    if not root:  # 若 not 根节点
        return True  # 返回 True
    q = deque([(root, None, None)])  # 把 deque([(根节点, None, None)]) 存入 节点
    while q:  # 循环，直到不满足「节点」
        node, low, high = q.popleft()  # 把 节点.popleft() 写入 node, low, high
        if (low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False  # 返回 False
        if node.left:  # 若 节点.左边界
            q.append((node.left, low, node.val))  # 把 (节点.左边界, low, 节点.值 追加到列表尾部
        if node.right:  # 若 节点.右边界
            q.append((node.right, node.val, high))  # 把 (节点.右边界, 节点.值, high 追加到列表尾部
    return True  # 返回 True


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


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(isValidBST(build_tree([2, 1, 3])))  # 打印输出
    print(isValidBST(build_tree([5, 1, 4, None, None, 3, 6])))  # 打印输出
