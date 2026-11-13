# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145053587
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def kthSmallest(root, k):  # 定义函数 kthSmallest（参数：根节点, 下标 k）
    stack = []  # 把 [] 存入 栈
    while root != None or len(stack):  # 循环，直到不满足「根节点 不等于 None or 长度(栈」
        while root != None:  # 循环，直到不满足「根节点 不等于 None」
            stack.append(root)  # 把 根节点 追加到列表尾部
            root = root.left  # 把 根节点.左边界 存入 根节点
        root = stack.pop()  # 把 栈 弹出 ) 存入 根节点
        k -= 1  # 下标 k累减 1
        if k == 0:  # 若 下标 k 等于 0
            break  # 跳出循环
        root = root.right  # 把 根节点.右边界 存入 根节点
    return root.val  # 返回 根节点.值


def build_bst(vals):  # 定义函数 build_bst（参数：vals）
    # vals: list of values in level-order, None for missing
    if not vals:  # 若 not vals
        return None  # 返回 None
    root = TreeNode(vals[0])  # 把 TreeNode(vals[0]) 存入 根节点
    queue = [root]  # 把 [根节点] 存入 队列
    i = 1  # 把 1 存入 下标 i
    while queue and i < len(vals):  # 循环，直到不满足「队列 and 下标 i 小于 长度(vals」
        node = queue.pop(0)  # 把 队列 弹出 0) 存入 节点
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.left = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 左边界
            queue.append(node.left)  # 把 节点.左边界 追加到列表尾部
        i += 1  # 下标 i累加 1
        if i < len(vals) and vals[i] is not None:  # 若 下标 i 小于 长度(vals) and vals[下标 i] is not None
            node.right = TreeNode(vals[i])  # 把 TreeNode(vals[下标 i]) 写入 右边界
            queue.append(node.right)  # 把 节点.右边界 追加到列表尾部
        i += 1  # 下标 i累加 1
    return root  # 返回 根节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    root = build_bst([3, 1, 4, None, 2])  # 把 build_bst([3, 1, 4, None, 2]) 存入 根节点
    print(kthSmallest(root, 1))  # 打印输出
    print(kthSmallest(root, 2))  # 打印输出
    print(kthSmallest(root, 3))  # 打印输出
    print(kthSmallest(root, 4))  # 打印输出
