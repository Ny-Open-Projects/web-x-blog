# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145030731
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def rightSideView(root):  # 定义函数 rightSideView（参数：根节点）
    if not root:  # 若 not 根节点
        return []  # 返回 []
    result = []  # 把 [] 存入 结果

    def dfs(node, depth):  # 定义函数 dfs（参数：节点, 深度）
        if not node:  # 若 not 节点
            return  # return
        if depth == len(result):  # 若 深度 等于 长度(结果
            result.append(node.val)  # 把 节点.值 追加到列表尾部
        dfs(node.right, depth + 1)  # dfs(节点.右边界, 深度 加 1)
        dfs(node.left, depth + 1)  # dfs(节点.左边界, 深度 加 1)

    dfs(root, 0)  # dfs(根节点, 0)
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build tree: [1,2,3,null,5,null,4]
    root = TreeNode(1)  # 把 TreeNode(1) 存入 根节点
    root.left = TreeNode(2)  # 把 TreeNode(2) 写入 左边界
    root.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    root.left.right = TreeNode(5)  # 把 TreeNode(5) 写入 右边界
    root.right.right = TreeNode(4)  # 把 TreeNode(4) 写入 右边界
    print(rightSideView(root))  # 打印输出
