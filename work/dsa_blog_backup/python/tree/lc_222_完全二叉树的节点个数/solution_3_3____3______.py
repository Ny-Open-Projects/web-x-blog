# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145052590
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def countNodes(root):  # 定义函数 countNodes（参数：根节点）
    if not root:  # 若 not 根节点
        return 0  # 返回 0

    def depth(node):  # 定义函数 depth（参数：节点）
        d = 0  # 把 0 存入 d
        while node:  # 循环，直到不满足「节点」
            d += 1  # d累加 1
            node = node.left  # 把 节点.左边界 存入 节点
        return d  # 返回 d

    left_depth = depth(root)  # 把 深度(根节点) 存入 left_depth
    right_depth = depth(root.right)  # 把 深度(根节点.右边界) 存入 right_depth
    if left_depth == right_depth:  # 若 left_depth 等于 right_depth
        return (1 << left_depth) - 1  # 返回 (1 小于 小于 left_depth) 减 1
    return (
        1 + countNodes(root.left) + countNodes(root.right)
    )  # 返回 1 加 countNodes(根节点.左边界) 加 countNodes(根节点.右边界)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build complete tree: [1,2,3,4,5,6]
    root = TreeNode(1)  # 把 TreeNode(1) 存入 根节点
    root.left = TreeNode(2)  # 把 TreeNode(2) 写入 左边界
    root.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    root.left.left = TreeNode(4)  # 把 TreeNode(4) 写入 左边界
    root.left.right = TreeNode(5)  # 把 TreeNode(5) 写入 右边界
    root.right.left = TreeNode(6)  # 把 TreeNode(6) 写入 左边界
    print(countNodes(root))  # 打印输出
