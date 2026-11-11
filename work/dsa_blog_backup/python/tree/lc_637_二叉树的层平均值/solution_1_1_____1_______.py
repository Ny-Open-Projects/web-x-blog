# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091296
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def averageOfLevels(root):  # 定义函数 averageOfLevels（参数：根节点）
    from collections import deque  # from collections import deque

    result = []  # 把 [] 存入 结果
    queue = deque([root])  # 把 deque([根节点]) 存入 队列
    while queue:  # 循环，直到不满足「队列」
        level_size = len(queue)  # 把 长度(队列) 存入 level_size
        total = 0  # 把 0 存入 总和
        for _ in range(level_size):  # 让 _ 从 level_size 遍历
            node = queue.popleft()  # 把 队列.popleft() 存入 节点
            total += node.val  # 总和累加 节点.值
            if node.left:  # 若 节点.左边界
                queue.append(node.left)  # 把 节点.左边界 追加到列表尾部
            if node.right:  # 若 节点.右边界
                queue.append(node.right)  # 把 节点.右边界 追加到列表尾部
        result.append(total / level_size)  # 把 总和 除以 level_size 追加到列表尾部
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    # build tree: [3,9,20,15,7]
    root = TreeNode(3)  # 把 TreeNode(3) 存入 根节点
    root.left = TreeNode(9)  # 把 TreeNode(9) 写入 左边界
    root.right = TreeNode(20)  # 把 TreeNode(20) 写入 右边界
    root.right.left = TreeNode(15)  # 把 TreeNode(15) 写入 左边界
    root.right.right = TreeNode(7)  # 把 TreeNode(7) 写入 右边界
    print(averageOfLevels(root))  # 打印输出
