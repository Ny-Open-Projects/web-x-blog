# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091772
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def insertIntoBST(root, val):  # 定义函数 insertIntoBST（参数：根节点, 值）
    if not root:
        return TreeNode(val)  # 若 not 根节点: return TreeNode(值
    if val < root.val:  # 若 值 小于 根节点.值
        root.left = insertIntoBST(root.left, val)  # 把 insertIntoBST(根节点.左边界, 值) 写入 左边界
    else:  # 否则
        root.right = insertIntoBST(root.right, val)  # 把 insertIntoBST(根节点.右边界, 值) 写入 右边界
    return root  # 返回 根节点


def to_list(root):  # 定义函数 to_list（参数：根节点）
    res = []  # 把 [] 存入 结果
    stack = [root]  # 把 [根节点] 存入 栈
    while stack:  # 循环，直到不满足「栈」
        node = stack.pop()  # 把 栈 弹出 ) 存入 节点
        if node:  # 若 节点
            res.append(node.val)  # 把 节点.值 追加到列表尾部
            stack.append(node.right)  # 把 节点.右边界 追加到列表尾部
            stack.append(node.left)  # 把 节点.左边界 追加到列表尾部
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
    print(to_list(insertIntoBST(root, 5)))  # 打印输出
