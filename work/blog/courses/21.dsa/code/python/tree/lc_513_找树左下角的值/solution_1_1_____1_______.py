# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145368911
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def findBottomLeftValue(root):  # 定义函数 findBottomLeftValue（参数：根节点）
    from collections import deque  # from collections import deque

    queue = deque([root])  # 把 deque([根节点]) 存入 队列
    leftmost = root.val  # 把 根节点.值 存入 leftmost
    while queue:  # 循环，直到不满足「队列」
        level_size = len(queue)  # 把 长度(队列) 存入 level_size
        for i in range(level_size):  # 让 下标 i 从 level_size 遍历
            node = queue.popleft()  # 把 队列.popleft() 存入 节点
            if i == 0:  # 若 下标 i 等于 0
                leftmost = node.val  # 把 节点.值 存入 leftmost
            if node.left:  # 若 节点.左边界
                queue.append(node.left)  # 把 节点.左边界 追加到列表尾部
            if node.right:  # 若 节点.右边界
                queue.append(node.right)  # 把 节点.右边界 追加到列表尾部
    return leftmost  # 返回 leftmost


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build tree: [1,2,3,4,null,5,6,null,null,7]
    root = TreeNode(1)  # 把 TreeNode(1) 存入 根节点
    root.left = TreeNode(2)  # 把 TreeNode(2) 写入 左边界
    root.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    root.left.left = TreeNode(4)  # 把 TreeNode(4) 写入 左边界
    root.right.left = TreeNode(5)  # 把 TreeNode(5) 写入 左边界
    root.right.right = TreeNode(6)  # 把 TreeNode(6) 写入 右边界
    root.right.left.left = TreeNode(7)  # 把 TreeNode(7) 写入 左边界
    print(findBottomLeftValue(root))  # 打印输出
