# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850725
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def rob(root):  # 定义函数 rob（参数：根节点）
    f = {}  # 把 {} 存入 f
    g = {}  # 把 {} 存入 g

    def dfs(node):  # 定义函数 dfs（参数：节点）
        if node is None:  # 若 节点 is None
            return  # return
        dfs(node.left)  # dfs(节点.左边界)
        dfs(node.right)  # dfs(节点.右边界)
        f[node] = (
            node.val + g.get(node.left, 0) + g.get(node.right, 0)
        )  # 把 节点.值 加 g 查找 节点.左边界, 0) 加 g 查找 节点.右边界, 0) 写入 f[node]
        g[node] = max(f.get(node.left, 0), g.get(node.left, 0)) + max(
            f.get(node.right, 0), g.get(node.right, 0)
        )

    dfs(root)  # dfs(根节点)
    return max(f.get(root, 0), g.get(root, 0))  # 返回 取较大值 f 查找 根节点, 0), g 查找 根节点, 0))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 示例树: 3 / \ 2 3 \ \ 3 1  -> 最大值为 7
    root = TreeNode(3)  # 把 TreeNode(3) 存入 根节点
    root.left = TreeNode(2)  # 把 TreeNode(2) 写入 左边界
    root.left.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    root.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    root.right.right = TreeNode(1)  # 把 TreeNode(1) 写入 右边界
    print(rob(root))  # 打印输出
