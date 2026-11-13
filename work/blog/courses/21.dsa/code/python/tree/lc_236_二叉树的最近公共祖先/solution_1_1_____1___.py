# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145083302
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def lowestCommonAncestor(root, p, q):  # 定义函数 lowestCommonAncestor（参数：根节点, 节点, 节点）
    if root is None or root is p or root is q:  # 若 根节点 is None or 根节点 is 节点 or 根节点 is 节点
        return root  # 返回 根节点
    left = lowestCommonAncestor(
        root.left, p, q
    )  # 把 lowestCommonAncestor(根节点.左边界, 节点, 节点) 存入 左边界
    right = lowestCommonAncestor(
        root.right, p, q
    )  # 把 lowestCommonAncestor(根节点.右边界, 节点, 节点) 存入 右边界
    if left and right:  # 若 左边界 and 右边界
        return root  # 返回 根节点
    return left if left else right  # 返回 左边界 if 左边界 else 右边界


def find(root, val):  # 定义函数 find（参数：根节点, 值）
    if root is None:  # 若 根节点 is None
        return None  # 返回 None
    if root.val == val:  # 若 根节点.值 等于 值
        return root  # 返回 根节点
    return find(root.left, val) or find(
        root.right, val
    )  # 返回 find(根节点.左边界, 值) or find(根节点.右边界, 值)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 构造示例树：root=3, left=5, right=1, 5的子节点9,7 ...
    root = TreeNode(3)  # 把 TreeNode(3) 存入 根节点
    root.left = TreeNode(5)  # 把 TreeNode(5) 写入 左边界
    root.right = TreeNode(1)  # 把 TreeNode(1) 写入 右边界
    root.left.left = TreeNode(6)  # 把 TreeNode(6) 写入 左边界
    root.left.right = TreeNode(2)  # 把 TreeNode(2) 写入 右边界
    root.right.left = TreeNode(0)  # 把 TreeNode(0) 写入 左边界
    root.right.right = TreeNode(8)  # 把 TreeNode(8) 写入 右边界
    root.left.right.left = TreeNode(7)  # 把 TreeNode(7) 写入 左边界
    root.left.right.right = TreeNode(4)  # 把 TreeNode(4) 写入 右边界
    p = find(root, 5)  # 把 find(根节点, 5) 存入 节点
    q = find(root, 1)  # 把 find(根节点, 1) 存入 节点
    ans = lowestCommonAncestor(root, p, q)  # 把 lowestCommonAncestor(根节点, 节点, 节点) 存入 答案
    print(ans.val if ans else None)  # 打印输出
