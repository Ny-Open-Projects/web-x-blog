# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145368911
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TreeNode:  # 定义类
    def __init__(self, val=0, left=None, right=None):  # 构造函数：初始化成员
        self.val = val  # 把 值 写入 值
        self.left = left  # 把 左边界 写入 左边界
        self.right = right  # 把 右边界 写入 右边界


def findBottomLeftValue(root):  # 定义函数 findBottomLeftValue（参数：根节点）
    ret = 0  # 把 0 存入 ret
    queue = [root]  # 把 [根节点] 存入 队列
    while len(queue):  # 循环，直到不满足「长度(队列」
        p = queue.pop(0)  # 把 队列 弹出 0) 存入 节点
        if p.right:  # 若 节点.右边界
            queue.append(p.right)  # 把 节点.右边界 追加到列表尾部
        if p.left:  # 若 节点.左边界
            queue.append(p.left)  # 把 节点.左边界 追加到列表尾部
        ret = p.val  # 把 节点.值 存入 ret
    return ret  # 返回 ret


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6))
    )  # TreeNode(3, None, TreeNode(6)))
    print(findBottomLeftValue(root))  # 打印输出
