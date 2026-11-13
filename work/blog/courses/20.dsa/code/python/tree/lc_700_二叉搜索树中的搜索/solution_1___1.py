# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091703
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def searchBST(root, val):  # 定义函数 searchBST（参数：根节点, 值）
    cur = root  # 把 根节点 存入 当前值
    while cur:  # 循环，直到不满足「当前值」
        if cur.val == val:  # 若 当前值.值 等于 值
            return cur  # 返回 当前值
        elif cur.val > val:  # 否则，若 当前值.值 超过 值
            cur = cur.left  # 把 当前值.左边界 存入 当前值
        else:  # 否则
            cur = cur.right  # 把 当前值.右边界 存入 当前值
    return None  # 返回 None


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build BST: [4,2,7,1,3]
    root = TreeNode(4)  # 把 TreeNode(4) 存入 根节点
    root.left = TreeNode(2)  # 把 TreeNode(2) 写入 左边界
    root.right = TreeNode(7)  # 把 TreeNode(7) 写入 右边界
    root.left.left = TreeNode(1)  # 把 TreeNode(1) 写入 左边界
    root.left.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    node = searchBST(root, 2)  # 把 searchBST(根节点, 2) 存入 节点
    print(node.val if node else None)  # 打印输出
