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
    from collections import deque  # from collections import deque

    result = []  # 把 [] 存入 结果
    queue = deque([root])  # 把 deque([根节点]) 存入 队列
    while queue:  # 循环，直到不满足「队列」
        level_size = len(queue)  # 把 长度(队列) 存入 level_size
        for i in range(level_size):  # 让 下标 i 从 level_size 遍历
            node = queue.popleft()  # 把 队列.popleft() 存入 节点
            if i == level_size - 1:  # 若 下标 i 等于 level_size 减 1
                result.append(node.val)  # 把 节点.值 追加到列表尾部
            if node.left:  # 若 节点.左边界
                queue.append(node.left)  # 把 节点.左边界 追加到列表尾部
            if node.right:  # 若 节点.右边界
                queue.append(node.right)  # 把 节点.右边界 追加到列表尾部
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build tree: [1,2,3,null,5,null,4]
    root = TreeNode(1)  # 把 TreeNode(1) 存入 根节点
    root.left = TreeNode(2)  # 把 TreeNode(2) 写入 左边界
    root.right = TreeNode(3)  # 把 TreeNode(3) 写入 右边界
    root.left.right = TreeNode(5)  # 把 TreeNode(5) 写入 右边界
    root.right.right = TreeNode(4)  # 把 TreeNode(4) 写入 右边界
    print(rightSideView(root))  # 打印输出
