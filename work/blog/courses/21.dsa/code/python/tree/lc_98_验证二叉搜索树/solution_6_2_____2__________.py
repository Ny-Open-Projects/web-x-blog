# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/131631290
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def isValidBST(root):  # 定义函数 isValidBST（参数：根节点）
    stack = []  # 把 [] 存入 栈
    inorder = float("-inf")  # 把 float(' 减 inf') 存入 inorder
    cur = root  # 把 根节点 存入 当前值
    while stack or cur:  # 循环，直到不满足「栈 or 当前值」
        while cur:  # 循环，直到不满足「当前值」
            stack.append(cur)  # 把 当前值 追加到列表尾部
            cur = cur.left  # 把 当前值.左边界 存入 当前值
        cur = stack.pop()  # 把 栈 弹出 ) 存入 当前值
        if cur.val <= inorder:  # 若 当前值.值 不超过 inorder
            return False  # 返回 False
        inorder = cur.val  # 把 当前值.值 存入 inorder
        cur = cur.right  # 把 当前值.右边界 存入 当前值
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # 合法 BST: 2 / \ 1 3
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))  # 把 TreeNode(2, TreeNode(1), TreeNode(3)) 存入 t1
    # 非法 BST: 5 / \ 1 4 / \ 3 6
    bad = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(isValidBST(t1))  # 打印输出
    print(isValidBST(bad))  # 打印输出
