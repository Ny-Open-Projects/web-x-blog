# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130907819
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def hasPathSum(root, targetSum):  # 定义函数 hasPathSum（参数：根节点, targetSum）
    if not root:  # 若 not 根节点
        return False  # 返回 False
    if not root.left and not root.right:  # 若 not 根节点.左边界 and not 根节点.右边界
        return root.val == targetSum  # 返回 根节点.值 等于 targetSum
    return hasPathSum(
        root.left, targetSum - root.val
    ) or hasPathSum(  # 返回 (hasPathSum(根节点.左边界, targetSum 减 根节点.值) or
        root.right, targetSum - root.val
    )  # hasPathSum(根节点.右边界, targetSum 减 根节点.值))


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
    root = TreeNode(5)  # 把 TreeNode(5) 存入 根节点
    root.left = TreeNode(4)  # 把 TreeNode(4) 写入 左边界
    root.right = TreeNode(8)  # 把 TreeNode(8) 写入 右边界
    root.left.left = TreeNode(11)  # 把 TreeNode(11) 写入 左边界
    root.left.left.left = TreeNode(7)  # 把 TreeNode(7) 写入 左边界
    root.left.left.right = TreeNode(2)  # 把 TreeNode(2) 写入 右边界
    root.right.left = TreeNode(13)  # 把 TreeNode(13) 写入 左边界
    root.right.right = TreeNode(4)  # 把 TreeNode(4) 写入 右边界
    root.right.right.right = TreeNode(1)  # 把 TreeNode(1) 写入 右边界
    print(hasPathSum(root, 22))  # 打印输出
