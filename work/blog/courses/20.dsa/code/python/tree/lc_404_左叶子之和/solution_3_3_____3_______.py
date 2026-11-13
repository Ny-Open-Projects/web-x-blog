# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145084192
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def isLeafNode(node):  # 定义函数 isLeafNode（参数：节点）
    return (
        node is not None and node.left is None and node.right is None
    )  # 返回 节点 is not None and 节点.左边界 is None and 节点.右边界 is None


def sumOfLeftLeaves(root):  # 定义函数 sumOfLeftLeaves（参数：根节点）
    if not root:  # 若 not 根节点
        return 0  # 返回 0

    def dfs(node):  # 定义函数 dfs（参数：节点）
        if not node:  # 若 not 节点
            return 0  # 返回 0
        total = 0  # 把 0 存入 总和
        if isLeafNode(node.left):  # 若 isLeafNode(节点.左边界
            total += node.left.val  # 总和累加 节点.左边界.值
        else:  # 否则
            total += dfs(node.left)  # 总和累加 dfs(节点.左边界)
        total += dfs(node.right)  # 总和累加 dfs(节点.右边界)
        return total  # 返回 总和

    return dfs(root)  # 返回 dfs(根节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)  # 把 TreeNode(3) 存入 根节点
    root.left = TreeNode(9)  # 把 TreeNode(9) 写入 左边界
    root.right = TreeNode(20)  # 把 TreeNode(20) 写入 右边界
    root.right.left = TreeNode(15)  # 把 TreeNode(15) 写入 左边界
    root.right.right = TreeNode(7)  # 把 TreeNode(7) 写入 右边界
    print(sumOfLeftLeaves(root))  # 打印输出
