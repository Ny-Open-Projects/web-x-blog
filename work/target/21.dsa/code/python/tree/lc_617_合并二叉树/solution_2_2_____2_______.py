# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145090998
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def mergeTrees(t1, t2):  # 定义函数 mergeTrees（参数：t1, t2）
    if not t1:  # 若 not t1
        return t2  # 返回 t2
    if not t2:  # 若 not t2
        return t1  # 返回 t1
    root = TreeNode(t1.val + t2.val)  # 把 TreeNode(t1.值 加 t2.值) 存入 根节点
    root.left = mergeTrees(t1.left, t2.left)  # 把 mergeTrees(t1.左边界, t2.左边界) 写入 左边界
    root.right = mergeTrees(t1.right, t2.right)  # 把 mergeTrees(t1.右边界, t2.右边界) 写入 右边界
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # t1 = [1,3,2,5], t2 = [2,1,3,null,4,null,7]
    t1 = TreeNode(1)  # 把 TreeNode(1) 存入 t1
    t1.left = TreeNode(3)  # 把 TreeNode(3) 写入 左边界
    t1.right = TreeNode(2)  # 把 TreeNode(2) 写入 右边界
    t1.left.left = TreeNode(5)  # 把 TreeNode(5) 写入 左边界
    t2 = TreeNode(2)  # 把 TreeNode(2) 存入 t2
    t2.left = TreeNode(1)  # 把 TreeNode(1) 写入 左边界
    t2.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    t2.left.right = TreeNode(4)  # 把 TreeNode(4) 写入 右边界
    t2.right.right = TreeNode(7)  # 把 TreeNode(7) 写入 右边界
    merged = mergeTrees(t1, t2)  # 把 mergeTrees(t1, t2) 存入 merged
    print(merged.val, merged.left.val, merged.right.val)  # 打印输出
